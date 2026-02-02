/**
 * BioBinConnect Voice Accessibility System
 * Provides voice input, voice commands, and text-to-speech for users with disabilities
 * Uses Web Speech API (100% Free, Built into browsers)
 */

class VoiceAccessibility {
  constructor() {
    this.recognition = null;
    this.synthesis = window.speechSynthesis;
    this.isListening = false;
    this.isEnabled = false;
    this.currentLanguage = "en-US";
    this.speechRate = 1.0;
    this.voiceCommands = {};
    this.activeInput = null;
    this.selectedMicrophoneId = null; // Selected microphone device ID
    
    // Continuous listening (hands-free mode)
    this.isContinuousListening = false;
    this.continuousRecognition = null;

    // Language support
    this.languages = {
      "en-US": "English",
      "hi-IN": "Hindi",
      "ml-IN": "Malayalam",
    };

    // Initialize
    this.init();
  }

  init() {
    // Check browser support
    if (
      !("webkitSpeechRecognition" in window) &&
      !("SpeechRecognition" in window)
    ) {
      console.warn("Speech Recognition not supported in this browser");
      return;
    }

    // Initialize Speech Recognition
    const SpeechRecognition =
      window.SpeechRecognition || window.webkitSpeechRecognition;
    this.recognition = new SpeechRecognition();
    this.recognition.continuous = false;
    this.recognition.interimResults = false;
    this.recognition.lang = this.currentLanguage;

    // Setup event listeners
    this.setupRecognitionListeners();

    // Load saved preferences
    this.loadPreferences();

    console.log("Voice Accessibility System Initialized");
  }

  setupRecognitionListeners() {
    if (!this.recognition) return;

    this.recognition.onstart = () => {
      this.isListening = true;
      this.updateListeningUI(true);
      
      // Quick audio feedback
      const utterance = new SpeechSynthesisUtterance('Listening');
      utterance.rate = 1.5;
      utterance.volume = 0.8;
      this.synthesis.speak(utterance);
    };

    this.recognition.onend = () => {
      this.isListening = false;
      this.updateListeningUI(false);
    };

    this.recognition.onresult = (event) => {
      const transcript = event.results[0][0].transcript;
      const confidence = event.results[0][0].confidence;

      console.log("Voice Input:", transcript, "Confidence:", confidence);

      // Audio feedback - tell user what was heard (Restored per user request)
      const feedbackText = `I heard: ${transcript}`;
      const utterance = new SpeechSynthesisUtterance(feedbackText);
      utterance.rate = 1.2;
      utterance.volume = 0.9;
      this.synthesis.speak(utterance);
      
      console.log(`Recognized: ${transcript}`);
      
      // Check if it's a voice command
      if (this.isVoiceCommand(transcript)) {
        this.executeVoiceCommand(transcript);
      } else if (this.activeInput) {
        // Fill the active input field
        const filled = this.fillInputField(this.activeInput, transcript);
        if (filled) {
            this.speak('Input filled');
        }
      } else {
         // If continuous listening is ON, we might want to be silent if it's just noise
         // But if it was a distinct phrase and not a command, say "Command not recognized"
         if (!this.isContinuousListening) {
             this.speak('Command not recognized');
         }
      }

    };

    this.recognition.onerror = (event) => {
      console.error("Speech recognition error:", event.error);
      this.isListening = false;
      this.updateListeningUI(false);

      let errorMessage = '';
      
      // Don't show error for "aborted" - it's usually intentional
      if (event.error === "aborted") {
        console.log("Recognition aborted - this is normal when switching inputs");
        return; // Don't speak or show alert
      }
      
      if (event.error === "no-speech") {
        errorMessage = "No speech detected. Please try again.";
      } else if (event.error === "not-allowed") {
        errorMessage = "Microphone access denied. Please enable microphone permissions in your browser settings.";
      } else if (event.error === "network") {
        errorMessage = "Network error. Please check your internet connection.";
      } else {
        errorMessage = `Voice recognition error: ${event.error}`;
      }
      
      // Speak the error message
      if (errorMessage) {
        this.speak(errorMessage);
      }
      
      // Also show visual alert for important errors
      if (event.error === "not-allowed" && typeof Swal !== 'undefined') {
        Swal.fire({
          icon: 'error',
          title: 'Microphone Access Required',
          text: errorMessage,
          confirmButtonColor: '#03A9F4'
        });
      }
    };
  }

  // Start listening for voice input
  startListening(inputElement = null) {
    if (!this.recognition) {
      alert(
        "Voice recognition is not supported in your browser. Please use Chrome, Edge, or Safari.",
      );
      return;
    }

    // Stop any existing recognition to prevent "aborted" error
    if (this.isListening) {
      try {
        this.recognition.stop();
      } catch (e) {
        console.log('Error stopping previous recognition:', e);
      }
      this.isListening = false;
      this.updateListeningUI(false);
    }
    
    // Pause continuous listening if active (don't stop it completely)
    const shouldResumeContinuous = this.isContinuousListening;
    if (shouldResumeContinuous && this.continuousRecognition) {
      try {
        this.continuousRecognition.abort(); // Use abort instead of stop
        console.log('Paused continuous listening for field input');
      } catch (e) {
        console.log('Error pausing continuous recognition:', e);
      }
    }

    this.activeInput = inputElement;

    // Wait a moment before starting new recognition
    setTimeout(() => {
      try {
        this.recognition.lang = this.currentLanguage;
        
        // Override onend to resume continuous listening
        const originalOnEnd = this.recognition.onend;
        this.recognition.onend = (event) => {
          this.isListening = false;
          this.updateListeningUI(false);
          
          // Resume continuous listening if it was active
          if (shouldResumeContinuous) {
            setTimeout(() => {
              if (this.isContinuousListening) {
                this.startContinuousListening();
                console.log('Resumed continuous listening after field input');
              }
            }, 500);
          }
          
          // Call original onend if it exists
          if (originalOnEnd) {
            originalOnEnd.call(this.recognition, event);
          }
        };
        
        this.recognition.start();
      } catch (error) {
        console.error("Error starting recognition:", error);
        this.speak("Error starting voice input. Please try again.");
        
        // Resume continuous if there was an error
        if (shouldResumeContinuous && this.isContinuousListening) {
          setTimeout(() => this.startContinuousListening(), 1000);
        }
      }
    }, 300); // Small delay to prevent abort error
  }

  stopListening() {
    if (this.recognition && this.isListening) {
      try {
        this.recognition.stop();
      } catch (e) {
        console.log('Error stopping recognition:', e);
      }
    }
  }

  // Text-to-Speech
  speak(text, options = {}) {
    if (!this.synthesis) {
      console.warn("Speech synthesis not supported");
      return;
    }

    // Don't cancel immediately - it might cut off the previous sentence too fast
    // Only cancel if it's a new "important" command or user pressed stop
    // this.synthesis.cancel(); 

    const utterance = new SpeechSynthesisUtterance(text);
    // Capture 'this' for the helper function
    const self = this;
    
    utterance.lang = this.currentLanguage;
    utterance.rate = options.rate || this.speechRate;
    utterance.pitch = options.pitch || 1.0;
    utterance.volume = options.volume || 1.0;

    // Helper to select voice safely
    function setVoice(availableVoices) {
        const voice = availableVoices.find((v) =>
          v.lang.startsWith(self.currentLanguage.split("-")[0])
        );
        if (voice) utterance.voice = voice;
    }

    // Robust voice selection
    const voices = this.synthesis.getVoices();
    if (voices.length > 0) {
        setVoice(voices);
    } else {
        // Wait for voices to load asynchronously (common in Chrome)
        this.synthesis.onvoiceschanged = () => {
            const loadedVoices = this.synthesis.getVoices();
            setVoice(loadedVoices);
        };
    }

    // Error handling
    utterance.onerror = (e) => {
        console.error('SpeechSynthesis Error:', e);
        // If not-allowed, try to resume and speak again once? 
        // Risk of infinite loop, so just log for now.
    };

    console.log(`Speaking: "${text}"`);
    
    // CRITICAL FIX: Chrome bug workaround
    // 1. Cancel any pending speech to reset state
    this.synthesis.cancel();
    
    // 2. Resume the synthesis engine (it often gets paused in Chrome)
    if (this.synthesis.paused) {
        this.synthesis.resume();
    }
    
    // 3. Speak
    this.synthesis.speak(utterance);
    
    // 4. Force resume again just in case
    if (this.synthesis.paused) {
        this.synthesis.resume();
    }
  }

  // Stop speaking
  stopSpeaking() {
    if (this.synthesis) {
      this.synthesis.cancel();
    }
  }

  // Read page content
  readPageContent() {
    const mainContent = document.querySelector("h1, .lead, main p");
    if (mainContent) {
      this.speak(mainContent.textContent);
    }
  }

  // Read form labels
  readFormLabel(inputElement) {
    const label = document.querySelector(`label[for="${inputElement.id}"]`);
    if (label) {
      this.speak(label.textContent);
    } else {
      const placeholder = inputElement.placeholder;
      if (placeholder) {
        this.speak(placeholder);
      }
    }
  }

  // Fill input field with voice input
  fillInputField(inputElement, text) {
    if (!inputElement) return;

    let cleanText = text.trim();
    
    // Simple capitalization commands (more reliable)
    if (cleanText.toLowerCase().startsWith('cap ')) {
      // "cap admin" -> "Admin"
      cleanText = cleanText.substring(4).trim();
      cleanText = cleanText.charAt(0).toUpperCase() + cleanText.slice(1).toLowerCase();
    } else if (cleanText.toLowerCase().startsWith('caps ')) {
      // "caps admin" -> "ADMIN"
      cleanText = cleanText.substring(5).trim();
      cleanText = cleanText.toUpperCase();
    }
    // Otherwise keep as-is

    // Handle special input types
    if (inputElement.type === "date") {
      const dateValue = this.parseDateFromVoice(cleanText);
      if (dateValue) {
        inputElement.value = dateValue;
      }
    } else if (inputElement.type === "number") {
      const numberValue = this.parseNumberFromVoice(cleanText);
      if (numberValue !== null) {
        inputElement.value = numberValue;
      }
    } else {
      // Regular text input
      inputElement.value = cleanText;
    }

    // Trigger change event
    inputElement.dispatchEvent(new Event("change", { bubbles: true }));
    inputElement.dispatchEvent(new Event("input", { bubbles: true }));

    // Provide feedback
    this.speak("Filled");

    // Visual feedback
    inputElement.classList.add("voice-filled");
    setTimeout(() => {
      inputElement.classList.remove("voice-filled");
    }, 1000);
  }

  // Register voice command
  registerCommand(command, callback, description = "") {
    const normalizedCommand = command.toLowerCase();
    this.voiceCommands[normalizedCommand] = {
      callback,
      description,
      patterns: this.generateCommandPatterns(normalizedCommand),
    };
  }

  // Generate command patterns for better matching
  generateCommandPatterns(command) {
    return [
      command,
      command.replace(/\s+/g, ""),
      `go to ${command}`,
      `open ${command}`,
      `show ${command}`,
      `navigate to ${command}`,
    ];
  }

  // Check if transcript is a voice command
  isVoiceCommand(transcript) {
    const normalized = transcript.toLowerCase().trim();

    for (const [command, data] of Object.entries(this.voiceCommands)) {
      if (data.patterns.some((pattern) => normalized.includes(pattern))) {
        return true;
      }
    }

    return false;
  }

  // Execute voice command
  executeVoiceCommand(transcript) {
    const normalized = transcript.toLowerCase().trim();

    for (const [command, data] of Object.entries(this.voiceCommands)) {
      if (data.patterns.some((pattern) => normalized.includes(pattern))) {
        // Friendlier feedback
        let actionWord = 'Okay';
        if (command.includes('go to') || command.includes('navigate') || command.includes('contact') || command.includes('about')) {
            actionWord = 'Navigating';
        } else if (command.includes('show') || command.includes('open')) {
            actionWord = 'Opening';
        } else if (command.includes('fill')) {
            actionWord = 'Filling';
        }
        
        this.speak(`${actionWord}...`);
        data.callback();
        return;
      }
    }
  }

  // Helper: Parse date from voice input
  parseDateFromVoice(text) {
    const today = new Date();
    const normalized = text.toLowerCase();

    if (normalized.includes("today")) {
      return this.formatDate(today);
    } else if (normalized.includes("tomorrow")) {
      const tomorrow = new Date(today);
      tomorrow.setDate(tomorrow.getDate() + 1);
      return this.formatDate(tomorrow);
    }

    // Try to parse date patterns
    const dateMatch = text.match(/(\d{1,2})[\/\-](\d{1,2})[\/\-](\d{2,4})/);
    if (dateMatch) {
      const [_, day, month, year] = dateMatch;
      const fullYear = year.length === 2 ? `20${year}` : year;
      return `${fullYear}-${month.padStart(2, "0")}-${day.padStart(2, "0")}`;
    }

    return null;
  }

  // Helper: Parse number from voice input
  parseNumberFromVoice(text) {
    // Convert word numbers to digits
    const wordToNumber = {
      zero: 0,
      one: 1,
      two: 2,
      three: 3,
      four: 4,
      five: 5,
      six: 6,
      seven: 7,
      eight: 8,
      nine: 9,
      ten: 10,
      twenty: 20,
      thirty: 30,
      forty: 40,
      fifty: 50,
      sixty: 60,
      seventy: 70,
      eighty: 80,
      ninety: 90,
      hundred: 100,
      thousand: 1000,
    };

    const normalized = text.toLowerCase();

    // Try to extract numeric value
    const numberMatch = text.match(/\d+/);
    if (numberMatch) {
      return parseInt(numberMatch[0]);
    }

    // Try word conversion
    for (const [word, value] of Object.entries(wordToNumber)) {
      if (normalized.includes(word)) {
        return value;
      }
    }

    return null;
  }

  // Format date to YYYY-MM-DD
  formatDate(date) {
    const year = date.getFullYear();
    const month = String(date.getMonth() + 1).padStart(2, "0");
    const day = String(date.getDate()).padStart(2, "0");
    return `${year}-${month}-${day}`;
  }

  // Update listening UI
  updateListeningUI(isListening) {
    const micButtons = document.querySelectorAll(".voice-mic-btn");
    micButtons.forEach((btn) => {
      if (isListening) {
        btn.classList.add("listening");
        btn.innerHTML = '<i class="fa fa-microphone-slash"></i>';
      } else {
        btn.classList.remove("listening");
        btn.innerHTML = '<i class="fa fa-microphone"></i>';
      }
    });
  }

  // Change language
  setLanguage(langCode) {
    if (this.languages[langCode]) {
      this.currentLanguage = langCode;
      if (this.recognition) {
        this.recognition.lang = langCode;
      }
      this.savePreferences();
      this.speak(`Language changed to ${this.languages[langCode]}`);
    }
  }

  // Change speech rate
  setSpeechRate(rate) {
    this.speechRate = Math.max(0.5, Math.min(2.0, rate));
    this.savePreferences();
  }
  
  // Set microphone device
  setMicrophone(deviceId) {
    this.selectedMicrophoneId = deviceId;
    console.log('Selected microphone:', deviceId || 'Default');
    this.speak('Microphone selected');
  }

  // Save preferences to localStorage
  savePreferences() {
    const prefs = {
      language: this.currentLanguage,
      speechRate: this.speechRate,
      enabled: this.isEnabled,
      continuousListening: this.isContinuousListening,
      selectedMic: this.selectedMicrophoneId
    };
    try {
        localStorage.setItem("voiceAccessibilityPrefs", JSON.stringify(prefs));
    } catch (e) {
        console.error("Failed to save preferences:", e);
    }
  }

  // Load preferences from localStorage
  loadPreferences() {
    const saved = localStorage.getItem("voiceAccessibilityPrefs");
    if (saved) {
      try {
        const prefs = JSON.parse(saved);
        this.currentLanguage = prefs.language || "en-US";
        this.speechRate = prefs.speechRate || 1.0;
        this.selectedMicrophoneId = prefs.selectedMic || null;

        if (this.recognition) {
          this.recognition.lang = this.currentLanguage;
        }
        
        // Restore enabled state
        if (prefs.enabled) {
          console.log('Restoring enabled state...');
          this.isEnabled = true;
          
          // Make sure toolbar knows about it if it exists
          if (window.accessibilityToolbar) {
              window.accessibilityToolbar.updateVoiceInputButton(true);
          }
          
          // Start mic monitoring if available
          if (this.startMicLevelMonitoring) {
              this.startMicLevelMonitoring();
          }
          
          // Restore continuous listening if it was active
          if (prefs.continuousListening) {
             console.log('Restoring continuous listening...');
             this.isContinuousListening = true;
             // Attempt to start after a brief delay
             setTimeout(() => {
                 this.startContinuousListening();
             }, 500);
          }
        }
      } catch (error) {
        console.error("Error loading preferences:", error);
      }
    }
  }

  // Enable/disable voice accessibility
  toggle() {
    this.isEnabled = !this.isEnabled;
    this.savePreferences();

    if (this.isEnabled) {
      // alert('Voice accessibility enabled'); // Debug feedback
      this.speak("Voice accessibility enabled");
    }

    return this.isEnabled;
  }
  
  // AI-powered fuzzy matching for voice commands
  fuzzyMatchCommand(transcript) {
    // Replace common misheard words
    let matched = transcript;
    
    // "full" → "fill"
    matched = matched.replace(/\bfull\b/g, 'fill');
    matched = matched.replace(/\bfool\b/g, 'fill');
    matched = matched.replace(/\bfeel\b/g, 'fill');
    matched = matched.replace(/\bphil\b/g, 'fill');
    
    // "go to" variations
    matched = matched.replace(/\bgoto\b/g, 'go to');
    matched = matched.replace(/\bgot to\b/g, 'go to');
    matched = matched.replace(/\bgo 2\b/g, 'go to');
    matched = matched.replace(/\bgotta\b/g, 'go to');
    matched = matched.replace(/\bgo two\b/g, 'go to');
    
    // Single word shortcuts
    if (matched === 'email' || matched === 'emails') {
      matched = 'fill email';
    }
    if (matched === 'password' || matched === 'passwords') {
      matched = 'fill password';
    }
    if (matched === 'username' || matched === 'user name') {
      matched = 'fill username';
    }
    
    // Common variations
    matched = matched.replace(/\bpasswrd\b/g, 'password');
    matched = matched.replace(/\busernam\b/g, 'username');
    
    return matched;
  }
  
  // Toggle continuous listening (hands-free mode)
  toggleContinuousListening() {
    console.log('toggleContinuousListening called, current state:', this.isContinuousListening);
    this.isContinuousListening = !this.isContinuousListening;
    this.savePreferences(); // Save state immediately
    
    // Update toolbar if it exists
    if (window.accessibilityToolbar) {
        window.accessibilityToolbar.updateContinuousListeningButton(this.isContinuousListening);
    }
    
    if (this.isContinuousListening) {
      console.log('Starting continuous listening...');
      this.startContinuousListening();
      this.speak('Hands-free mode enabled');
    } else {
      console.log('Stopping continuous listening...');
      this.stopContinuousListening();
      this.speak('Hands-free mode disabled');
    }
    
    return this.isContinuousListening;
  }
  
  // Start continuous listening
  startContinuousListening() {
    console.log('startContinuousListening called');
    if (!this.recognition) {
      console.error('No recognition object available!');
      return;
    }
    
    // Create a continuous recognition instance
    const SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition;
    if (!SpeechRecognition) {
      console.error('SpeechRecognition not supported!');
      this.speak('Voice recognition not supported in this browser');
      return;
    }
    
    console.log('Creating continuous recognition instance...');
    this.continuousRecognition = new SpeechRecognition();
    this.continuousRecognition.continuous = true; // Keep listening
    this.continuousRecognition.interimResults = false;
    this.continuousRecognition.lang = this.currentLanguage;
    
    this.continuousRecognition.onstart = () => {
      console.log('✅ Continuous recognition STARTED successfully');
    };
    
    this.continuousRecognition.onresult = (event) => {
      const transcript = event.results[event.results.length - 1][0].transcript.toLowerCase().trim();
      console.log('🎤 Continuous listening heard:', transcript);
      
      // AI-powered fuzzy matching - recognize similar commands
      const fuzzyCommand = this.fuzzyMatchCommand(transcript);
      console.log('🤖 AI matched command:', fuzzyCommand);
      
      // Check for "fill [field]" commands with fuzzy matching
      if (fuzzyCommand.includes('fill email') || fuzzyCommand.includes('full email') || transcript === 'email') {
        console.log('Detected: fill email command');
        const emailInput = document.querySelector('input[type="email"]');
        if (emailInput) {
          this.speak('Say your email address now');
          // Longer delay to give user time to prepare
          setTimeout(() => {
            console.log('🎤 Starting to listen for email...');
            this.startListening(emailInput);
          }, 2000); // 2 seconds delay
        } else {
          console.warn('No email field found on page');
          this.speak('No email field found');
        }
      } else if (fuzzyCommand.includes('fill password') || fuzzyCommand.includes('full password') || transcript === 'password') {
        console.log('Detected: fill password command');
        const passwordInput = document.querySelector('input[type="password"]');
        if (passwordInput) {
          this.speak('Say your password now');
          setTimeout(() => {
            console.log('🎤 Starting to listen for password...');
            this.startListening(passwordInput);
          }, 2000); // 2 seconds delay
        } else {
          console.warn('No password field found on page');
          this.speak('No password field found');
        }
      } else if (fuzzyCommand.includes('fill username') || fuzzyCommand.includes('full username') || transcript === 'username') {
        console.log('Detected: fill username command');
        const usernameInput = document.querySelector('input[name="username"], input[id="username"]');
        if (usernameInput) {
          this.speak('Say your username now');
          setTimeout(() => {
            console.log('🎤 Starting to listen for username...');
            this.startListening(usernameInput);
          }, 2000);
        } else {
          console.warn('No username field found on page');
          this.speak('No username field found');
        }
      } else if (fuzzyCommand.includes('fill name') || fuzzyCommand.includes('full name') || transcript === 'name') {
        console.log('Detected: fill name command');
        const nameInput = document.querySelector('input[name*="name"], input[placeholder*="name"]');
        if (nameInput) {
          this.speak('Say your name now');
          setTimeout(() => {
            console.log('🎤 Starting to listen for name...');
            this.startListening(nameInput);
          }, 2000);
        } else {
          console.warn('No name field found on page');
          this.speak('No name field found');
        }
      } else if (this.isVoiceCommand(fuzzyCommand)) {
        console.log('Detected voice command:', fuzzyCommand);
        this.executeVoiceCommand(fuzzyCommand);
      } else {
        console.log('No matching command found for:', transcript);
        // Provide helpful feedback
        this.speak('Command not available ask admin to add it');
      }
    };
    
    this.continuousRecognition.onerror = (event) => {
      console.error('Continuous recognition error:', event.error);
      
      // Ignore abort errors - they're intentional when pausing for field input
      if (event.error === 'aborted') {
        console.log('Continuous listening aborted - will resume after field input');
        return;
      }
      
      if (event.error === 'no-speech') {
        // Restart if no speech detected
        if (this.isContinuousListening) {
          setTimeout(() => {
            if (this.continuousRecognition && this.isContinuousListening) {
              try {
                this.continuousRecognition.start();
              } catch (e) {
                console.log('Already listening');
              }
            }
          }, 1000);
        }
      } else if (event.error === 'not-allowed') {
        this.speak('Microphone access denied. Please enable microphone permissions.');
        this.isContinuousListening = false;
      }
    };
    
    this.continuousRecognition.onend = () => {
      // Auto-restart continuous listening
      if (this.isContinuousListening) {
        setTimeout(() => {
          if (this.continuousRecognition && this.isContinuousListening) {
            try {
              this.continuousRecognition.start();
            } catch (e) {
              console.log('Already listening');
            }
          }
        }, 500);
      }
    };
    
    try {
      this.continuousRecognition.start();
      console.log('Continuous listening started');
    } catch (error) {
      console.error('Error starting continuous recognition:', error);
    }
  }
  
  // Stop continuous listening
  stopContinuousListening() {
    if (this.continuousRecognition) {
      this.continuousRecognition.stop();
      this.continuousRecognition = null;
      console.log('Continuous listening stopped');
    }
  }
  
  // Pause continuous listening temporarily
  pauseContinuousListening() {
    if (this.continuousRecognition) {
      try {
        this.continuousRecognition.stop();
      } catch (e) {
        console.log('Error pausing continuous listening:', e);
      }
    }
  }
  
  // Resume continuous listening
  resumeContinuousListening() {
    if (this.isContinuousListening && this.continuousRecognition) {
      try {
        this.continuousRecognition.start();
        console.log('Continuous listening resumed');
      } catch (e) {
        console.log('Error resuming continuous listening:', e);
      }
    }
  }
}

// Create global instance
window.voiceAccessibility = new VoiceAccessibility();
