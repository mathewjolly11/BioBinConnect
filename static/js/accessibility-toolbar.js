/**
 * Accessibility Toolbar Component
 * Floating toolbar for voice and accessibility controls
 */

class AccessibilityToolbar {
    constructor() {
        this.isVisible = false; // Default to hidden/minimized
        this.isMinimized = false;
        this.init();
    }
    
    init() {
        this.createToolbar();
        this.attachEventListeners();
        this.loadState();
        
        // Ensure correct initial state
        if (!this.isVisible) {
            const toolbar = document.getElementById('accessibility-toolbar');
            if (toolbar) toolbar.style.display = 'none';
            this.showReopenButton();
        }
    }
    
    createToolbar() {
        const toolbar = document.createElement('div');
        toolbar.id = 'accessibility-toolbar';
        toolbar.className = 'accessibility-toolbar';
        toolbar.innerHTML = `
            <div class="toolbar-header">
                <h6><i class="fa fa-universal-access"></i> Accessibility</h6>
                <button class="toolbar-minimize" title="Minimize">
                    <i class="fa fa-minus"></i>
                </button>
                <button class="toolbar-close" title="Close">
                    <i class="fa fa-times"></i>
                </button>
            </div>
            
            <div class="toolbar-content">
                <!-- Voice Input Section -->
                <div class="toolbar-section">
                    <h6><i class="fa fa-microphone"></i> Voice Input</h6>
                    <button class="toolbar-btn" id="toggleVoiceInput" title="Toggle voice input for forms">
                        <i class="fa fa-microphone"></i>
                        <span>Enable Voice Input</span>
                    </button>
                    
                    <button class="toolbar-btn" id="toggleContinuousListening" title="Enable hands-free continuous listening" style="display: none;">
                        <i class="fa fa-microphone-alt"></i>
                        <span>Enable Hands-Free Mode</span>
                    </button>
                    
                    <!-- Microphone Selector -->
                    <div class="toolbar-control" id="micSelector" style="display: none;">
                        <label><i class="fa fa-microphone"></i> Select Microphone:</label>
                        <select id="microphoneSelect" class="toolbar-select">
                            <option value="">Default Microphone</option>
                        </select>
                    </div>
                    
                    <!-- Microphone Level Indicator -->
                    <div class="mic-level-container" id="micLevelContainer" style="display: none;">
                        <label><i class="fa fa-signal"></i> Mic Level:</label>
                        <div class="mic-level-bar">
                            <div class="mic-level-fill" id="micLevelFill"></div>
                        </div>
                        <span class="mic-level-text" id="micLevelText">0%</span>
                    </div>
                    
                    <div class="toolbar-control" id="continuousListeningInfo" style="display: none;">
                        <small class="text-muted">
                            <i class="fa fa-info-circle"></i> Hands-free mode: Just say "fill [field name]" then speak your input.
                        </small>
                    </div>
                </div>
                
                <!-- Text-to-Speech Section -->
                <div class="toolbar-section">
                    <h6><i class="fa fa-volume-up"></i> Text-to-Speech</h6>
                    <button class="toolbar-btn" id="readPage" title="Read page content aloud">
                        <i class="fa fa-book"></i>
                        <span>Read Page</span>
                    </button>
                    <button class="toolbar-btn" id="stopSpeaking" title="Stop reading">
                        <i class="fa fa-stop"></i>
                        <span>Stop</span>
                    </button>
                    
                    <div class="toolbar-control">
                        <label>Speech Rate:</label>
                        <input type="range" id="speechRate" min="0.5" max="2" step="0.1" value="1">
                        <span id="speechRateValue">1.0x</span>
                    </div>
                </div>
                
                <!-- Language Selection -->
                <div class="toolbar-section">
                    <h6><i class="fa fa-language"></i> Language</h6>
                    <select id="languageSelect" class="toolbar-select">
                        <option value="en-US">English</option>
                        <option value="hi-IN">हिंदी (Hindi)</option>
                        <option value="ml-IN">മലയാളം (Malayalam)</option>
                    </select>
                </div>
                
                <!-- Voice Commands Help -->
                <div class="toolbar-section">
                    <h6><i class="fa fa-question-circle"></i> Voice Commands</h6>
                    <button class="toolbar-btn" id="showCommands" title="Show available voice commands">
                        <i class="fa fa-list"></i>
                        <span>Show Commands</span>
                    </button>
                </div>
                
                <!-- Keyboard Shortcuts -->
                <div class="toolbar-section">
                    <h6><i class="fa fa-keyboard-o"></i> Shortcuts</h6>
                    <div class="shortcuts-info">
                        <small>
                            <strong>Ctrl + Shift + V:</strong> Toggle Voice<br>
                            <strong>Ctrl + Shift + S:</strong> Stop Reading<br>
                            <strong>Ctrl + Shift + H:</strong> Hands-Free Mode
                        </small>
                    </div>
                </div>
            </div>
            
            <div class="toolbar-footer">
                <small>Powered by Web Speech API</small>
            </div>
        `;
        
        document.body.appendChild(toolbar);
    }
    
    attachEventListeners() {
        // Minimize/Maximize
        document.querySelector('.toolbar-minimize').addEventListener('click', () => {
            this.toggleMinimize();
        });
        
        // Close
        document.querySelector('.toolbar-close').addEventListener('click', () => {
            this.hide();
        });
        
        // Toggle Voice Input
        document.getElementById('toggleVoiceInput').addEventListener('click', () => {
            try {
                if (!window.voiceAccessibility) {
                    alert('Error: Voice Accessibility system not initialized. Please refresh the page.');
                    return;
                }
                
                const enabled = window.voiceAccessibility.toggle();
                this.updateVoiceInputButton(enabled);
                
                if (enabled) {
                    this.enableVoiceInputForAllForms();
                    // Show continuous listening option
                    document.getElementById('toggleContinuousListening').style.display = 'flex';
                    // Show mic selector
                    document.getElementById('micSelector').style.display = 'block';
                    this.populateMicrophoneList();
                    // Show mic level indicator
                    document.getElementById('micLevelContainer').style.display = 'block';
                    // Start mic level monitoring
                    if (window.voiceAccessibility.startMicLevelMonitoring) {
                        window.voiceAccessibility.startMicLevelMonitoring();
                    }
                } else {
                    this.disableVoiceInputForAllForms();
                    // Hide continuous listening option
                    document.getElementById('toggleContinuousListening').style.display = 'none';
                    document.getElementById('continuousListeningInfo').style.display = 'none';
                    // Hide mic selector
                    document.getElementById('micSelector').style.display = 'none';
                    // Hide mic level indicator
                    document.getElementById('micLevelContainer').style.display = 'none';
                    // Stop mic level monitoring
                    if (window.voiceAccessibility.stopMicLevelMonitoring) {
                        window.voiceAccessibility.stopMicLevelMonitoring();
                    }
                }
            } catch (err) {
                console.error('Error toggling voice input:', err);
                alert('Error toggling voice input: ' + err.message);
            }
        });
        
        // Microphone selection change
        document.getElementById('microphoneSelect').addEventListener('change', (e) => {
            const deviceId = e.target.value;
            if (window.voiceAccessibility.setMicrophone) {
                window.voiceAccessibility.setMicrophone(deviceId);
            }
        });
        
        // Toggle Continuous Listening (Hands-Free Mode)
        document.getElementById('toggleContinuousListening').addEventListener('click', () => {
            const enabled = window.voiceAccessibility.toggleContinuousListening();
            const btn = document.getElementById('toggleContinuousListening');
            const info = document.getElementById('continuousListeningInfo');
            
            if (enabled) {
                btn.classList.add('active');
                btn.querySelector('span').textContent = 'Disable Hands-Free Mode';
                info.style.display = 'block';
            } else {
                btn.classList.remove('active');
                btn.querySelector('span').textContent = 'Enable Hands-Free Mode';
                info.style.display = 'none';
            }
        });
        
        // Read Page
        document.getElementById('readPage').addEventListener('click', () => {
            window.voiceAccessibility.readPageContent();
        });
        
        // Stop Speaking
        document.getElementById('stopSpeaking').addEventListener('click', () => {
            window.voiceAccessibility.stopSpeaking();
        });
        
        // Speech Rate
        const speechRateSlider = document.getElementById('speechRate');
        speechRateSlider.addEventListener('input', (e) => {
            const rate = parseFloat(e.target.value);
            window.voiceAccessibility.setSpeechRate(rate);
            document.getElementById('speechRateValue').textContent = rate.toFixed(1) + 'x';
        });
        
        // Language Selection
        document.getElementById('languageSelect').addEventListener('change', (e) => {
            window.voiceAccessibility.setLanguage(e.target.value);
        });
        
        // Show Commands
        document.getElementById('showCommands').addEventListener('click', () => {
            this.showVoiceCommandsHelp();
        });
        
        // Keyboard Shortcuts
        document.addEventListener('keydown', (e) => {
            if (e.ctrlKey && e.shiftKey) {
                switch(e.key.toLowerCase()) {
                    case 'v':
                        e.preventDefault();
                        document.getElementById('toggleVoiceInput').click();
                        break;
                    // Removed 'r' case - conflicts with browser hard refresh
                    case 's':
                        e.preventDefault();
                        document.getElementById('stopSpeaking').click();
                        break;
                    case 'h':
                        e.preventDefault();
                        const continuousBtn = document.getElementById('toggleContinuousListening');
                        if (continuousBtn.style.display !== 'none') {
                            continuousBtn.click();
                        }
                        break;
                }
            }
        });
        
        // Make toolbar draggable
        this.makeDraggable();
    }
    
    enableVoiceInputForAllForms() {
        // Add microphone buttons to all text inputs INCLUDING PASSWORD FIELDS
        const inputs = document.querySelectorAll('input[type="text"], input[type="email"], input[type="tel"], input[type="number"], input[type="date"], input[type="password"], textarea');
        
        inputs.forEach(input => {
            if (input.classList.contains('voice-enabled')) return;
            
            input.classList.add('voice-enabled');
            
            // Create mic button
            const micBtn = document.createElement('button');
            micBtn.type = 'button';
            micBtn.className = 'voice-mic-btn';
            micBtn.innerHTML = '<i class="fa fa-microphone"></i>';
            micBtn.title = 'Click to use voice input';
            
            // Position button
            const wrapper = document.createElement('div');
            wrapper.className = 'voice-input-wrapper';
            input.parentNode.insertBefore(wrapper, input);
            wrapper.appendChild(input);
            wrapper.appendChild(micBtn);
            
            // Add click handler
            micBtn.addEventListener('click', () => {
                window.voiceAccessibility.startListening(input);
            });
            
            // Add focus handler to read label
            input.addEventListener('focus', () => {
                if (window.voiceAccessibility.isEnabled) {
                    window.voiceAccessibility.readFormLabel(input);
                }
            });
        });
    }
    
    disableVoiceInputForAllForms() {
        const wrappers = document.querySelectorAll('.voice-input-wrapper');
        wrappers.forEach(wrapper => {
            const input = wrapper.querySelector('input, textarea');
            const micBtn = wrapper.querySelector('.voice-mic-btn');
            
            if (input && micBtn) {
                wrapper.parentNode.insertBefore(input, wrapper);
                wrapper.remove();
                input.classList.remove('voice-enabled');
            }
        });
    }
    
    updateVoiceInputButton(enabled) {
        const btn = document.getElementById('toggleVoiceInput');
        const contBtn = document.getElementById('toggleContinuousListening');
        
        if (enabled) {
            btn.classList.add('active');
            btn.querySelector('span').textContent = 'Disable Voice Input';
            
            // Explicitly show hands-free button
            if (contBtn) {
                contBtn.style.display = 'flex';
                contBtn.style.visibility = 'visible'; // Ensure visibility
                console.log('Voice enabled: Showing hands-free button');
            }
        } else {
            btn.classList.remove('active');
            btn.querySelector('span').textContent = 'Enable Voice Input';
            
            // Hide hands-free button
            if (contBtn) contBtn.style.display = 'none';
        }
    }

    updateContinuousListeningButton(enabled) {
        const btn = document.getElementById('toggleContinuousListening');
        if (!btn) return;
        
        const statusInfo = document.getElementById('continuousListeningInfo');
        
        if (enabled) {
            btn.classList.add('active');
            btn.querySelector('span').textContent = 'Disable Hands-Free Mode';
            if (statusInfo) statusInfo.style.display = 'block';
        } else {
            btn.classList.remove('active');
            btn.querySelector('span').textContent = 'Enable Hands-Free Mode';
            if (statusInfo) statusInfo.style.display = 'none';
        }
    }
    
    showVoiceCommandsHelp() {
        const commands = window.voiceAccessibility.voiceCommands;
        let commandsList = '<ul class="commands-list">';
        
        for (const [command, data] of Object.entries(commands)) {
            commandsList += `<li><strong>"${command}"</strong> - ${data.description}</li>`;
        }
        
        commandsList += '</ul>';
        
        Swal.fire({
            title: '<i class="fa fa-microphone"></i> Available Voice Commands',
            html: `
                <div class="text-start">
                    <p>You can say any of these commands:</p>
                    ${commandsList}
                    <hr>
                    <p><strong>Tips:</strong></p>
                    <ul>
                        <li>Speak clearly and at normal pace</li>
                        <li>Commands work in any language you select</li>
                        <li>You can also use voice to fill form fields</li>
                    </ul>
                </div>
            `,
            icon: 'info',
            confirmButtonText: 'Got it!',
            confirmButtonColor: '#03A9F4',
            width: '600px'
        });
    }
    
    toggleMinimize() {
        const toolbar = document.getElementById('accessibility-toolbar');
        const content = toolbar.querySelector('.toolbar-content');
        const footer = toolbar.querySelector('.toolbar-footer');
        const minimizeBtn = toolbar.querySelector('.toolbar-minimize i');
        
        this.isMinimized = !this.isMinimized;
        
        if (this.isMinimized) {
            content.style.display = 'none';
            footer.style.display = 'none';
            minimizeBtn.className = 'fa fa-plus';
        } else {
            content.style.display = 'block';
            footer.style.display = 'block';
            minimizeBtn.className = 'fa fa-minus';
        }
        
        this.saveState();
    }
    
    hide() {
        const toolbar = document.getElementById('accessibility-toolbar');
        toolbar.style.display = 'none';
        this.isVisible = false;
        // Don't save state - allow toolbar to reappear on refresh
        // this.saveState();
        
        // Show the reopen button
        this.showReopenButton();
    }
    
    show() {
        const toolbar = document.getElementById('accessibility-toolbar');
        toolbar.style.display = 'block';
        this.isVisible = true;
        this.saveState();
        
        // Hide the reopen button
        this.hideReopenButton();
    }
    
    showReopenButton() {
        let reopenBtn = document.getElementById('accessibility-reopen-btn');
        if (!reopenBtn) {
            reopenBtn = document.createElement('button');
            reopenBtn.id = 'accessibility-reopen-btn';
            reopenBtn.className = 'accessibility-reopen-btn';
            reopenBtn.innerHTML = '<i class="fa fa-universal-access"></i>';
            reopenBtn.title = 'Open Accessibility Toolbar';
            reopenBtn.addEventListener('click', () => {
                this.show();
            });
            document.body.appendChild(reopenBtn);
        }
        reopenBtn.style.display = 'flex';
    }
    
    hideReopenButton() {
        const reopenBtn = document.getElementById('accessibility-reopen-btn');
        if (reopenBtn) {
            reopenBtn.style.display = 'none';
        }
    }
    
    makeDraggable() {
        const toolbar = document.getElementById('accessibility-toolbar');
        const header = toolbar.querySelector('.toolbar-header');
        
        let isDragging = false;
        let currentX;
        let currentY;
        let initialX;
        let initialY;
        
        header.addEventListener('mousedown', (e) => {
            if (e.target.closest('button')) return;
            
            isDragging = true;
            initialX = e.clientX - toolbar.offsetLeft;
            initialY = e.clientY - toolbar.offsetTop;
            header.style.cursor = 'grabbing';
        });
        
        document.addEventListener('mousemove', (e) => {
            if (!isDragging) return;
            
            e.preventDefault();
            currentX = e.clientX - initialX;
            currentY = e.clientY - initialY;
            
            toolbar.style.left = currentX + 'px';
            toolbar.style.top = currentY + 'px';
            toolbar.style.right = 'auto';
            toolbar.style.bottom = 'auto';
        });
        
        document.addEventListener('mouseup', () => {
            if (isDragging) {
                isDragging = false;
                header.style.cursor = 'grab';
                this.saveState();
            }
        });
    }
    
    saveState() {
        const toolbar = document.getElementById('accessibility-toolbar');
        const state = {
            visible: this.isVisible,
            minimized: this.isMinimized,
            position: {
                left: toolbar.style.left,
                right: toolbar.style.right,
                top: toolbar.style.top,
                bottom: toolbar.style.bottom
            }
        };
        localStorage.setItem('accessibilityToolbarState', JSON.stringify(state));
    }
    
    loadState() {
        const saved = localStorage.getItem('accessibilityToolbarState');
        if (saved) {
            try {
                const state = JSON.parse(saved);
                const toolbar = document.getElementById('accessibility-toolbar');
                
                // Always show toolbar on page load (ignore saved visibility)
                // if (!state.visible) {
                //     this.hide();
                // }
                
                if (state.minimized) {
                    this.toggleMinimize();
                }
                
                if (state.position.left || state.position.right) {
                    if (state.position.left) {
                        toolbar.style.left = state.position.left;
                        toolbar.style.right = 'auto';
                    } else {
                        toolbar.style.right = state.position.right;
                        toolbar.style.left = 'auto';
                    }
                    if (state.position.top) {
                        toolbar.style.top = state.position.top;
                        toolbar.style.bottom = 'auto';
                    } else if (state.position.bottom) {
                        toolbar.style.bottom = state.position.bottom;
                        toolbar.style.top = 'auto';
                    }
                }
            } catch (error) {
                console.error('Error loading toolbar state:', error);
            }
        }
    }
    
    async populateMicrophoneList() {
        try {
            const devices = await navigator.mediaDevices.enumerateDevices();
            const audioInputs = devices.filter(device => device.kind === 'audioinput');
            
            const select = document.getElementById('microphoneSelect');
            if (!select) return;
            
            select.innerHTML = '<option value="">Default Microphone</option>';
            
            audioInputs.forEach((device, index) => {
                const option = document.createElement('option');
                option.value = device.deviceId;
                option.textContent = device.label || `Microphone ${index + 1}`;
                select.appendChild(option);
            });
            
            console.log(`Found ${audioInputs.length} microphone(s)`);
        } catch (error) {
            console.error('Error enumerating microphones:', error);
        }
    }
}

// Initialize toolbar when DOM is ready
document.addEventListener('DOMContentLoaded', () => {
    window.accessibilityToolbar = new AccessibilityToolbar();
    
    // Sync state with voice accessibility immediately
    if (window.voiceAccessibility && window.voiceAccessibility.isEnabled) {
        // If voice accessibility loaded first and read its prefs
        window.accessibilityToolbar.updateVoiceInputButton(true);
        
        // Show extra controls
        if (window.voiceAccessibility.isContinuousListening) {
            const contBtn = document.getElementById('toggleContinuousListening');
            if (contBtn) contBtn.style.display = 'flex';
            const contInfo = document.getElementById('continuousListeningInfo');
            if (contInfo) contInfo.style.display = 'block';
        }
        
        const micSelector = document.getElementById('micSelector');
        if (micSelector) {
            micSelector.style.display = 'block';
            window.accessibilityToolbar.populateMicrophoneList();
        }
        
        const micLevel = document.getElementById('micLevelContainer');
        if (micLevel) micLevel.style.display = 'block';
    }
});
