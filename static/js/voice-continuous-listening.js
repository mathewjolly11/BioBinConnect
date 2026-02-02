// Add continuous listening functionality to voice-accessibility.js
// This will be appended to the existing VoiceAccessibility class

// Add these properties to the constructor (lines 8-16):
// this.isContinuousListening = false;
// this.continuousRecognition = null;

// Add this method to the VoiceAccessibility class:

VoiceAccessibility.prototype.toggleContinuousListening = function() {
    this.isContinuousListening = !this.isContinuousListening;
    
    if (this.isContinuousListening) {
        this.startContinuousListening();
        this.speak('Hands-free mode enabled. Say fill email, fill password, or any voice command.');
    } else {
        this.stopContinuousListening();
        this.speak('Hands-free mode disabled');
    }
    
    return this.isContinuousListening;
};

VoiceAccessibility.prototype.startContinuousListening = function() {
    if (!this.recognition) return;
    
    // Create a continuous recognition instance
    const SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition;
    this.continuousRecognition = new SpeechRecognition();
    this.continuousRecognition.continuous = true; // Keep listening
    this.continuousRecognition.interimResults = false;
    this.continuousRecognition.lang = this.currentLanguage;
    
    this.continuousRecognition.onresult = (event) => {
        const transcript = event.results[event.results.length - 1][0].transcript.toLowerCase().trim();
        console.log('Continuous listening heard:', transcript);
        
        // Check for "fill [field]" commands
        if (transcript.includes('fill email')) {
            const emailInput = document.querySelector('input[type="email"]');
            if (emailInput) {
                this.speak('Say your email address');
                setTimeout(() => this.startListening(emailInput), 1000);
            }
        } else if (transcript.includes('fill password')) {
            const passwordInput = document.querySelector('input[type="password"]');
            if (passwordInput) {
                this.speak('Say your password');
                setTimeout(() => this.startListening(passwordInput), 1000);
            }
        } else if (transcript.includes('fill username')) {
            const usernameInput = document.querySelector('input[name="username"], input[id="username"]');
            if (usernameInput) {
                this.speak('Say your username');
                setTimeout(() => this.startListening(usernameInput), 1000);
            }
        } else if (this.isVoiceCommand(transcript)) {
            // Execute voice commands
            this.executeVoiceCommand(transcript);
        }
    };
    
    this.continuousRecognition.onerror = (event) => {
        console.error('Continuous recognition error:', event.error);
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
    } catch (error) {
        console.error('Error starting continuous recognition:', error);
    }
};

VoiceAccessibility.prototype.stopContinuousListening = function() {
    if (this.continuousRecognition) {
        this.continuousRecognition.stop();
        this.continuousRecognition = null;
    }
};
