// Microphone Level Monitoring
// Add this to voice-accessibility.js

VoiceAccessibility.prototype.startMicLevelMonitoring = function() {
  if (!navigator.mediaDevices || !navigator.mediaDevices.getUserMedia) {
    console.warn('getUserMedia not supported');
    return;
  }
  
  navigator.mediaDevices.getUserMedia({ audio: true })
    .then(stream => {
      const audioContext = new (window.AudioContext || window.webkitAudioContext)();
      const microphone = audioContext.createMediaStreamSource(stream);
      const analyser = audioContext.createAnalyser();
      analyser.fftSize = 256;
      
      microphone.connect(analyser);
      
      const bufferLength = analyser.frequencyBinCount;
      const dataArray = new Uint8Array(bufferLength);
      
      const updateLevel = () => {
        if (!this.isEnabled) {
          stream.getTracks().forEach(track => track.stop());
          return;
        }
        
        analyser.getByteFrequencyData(dataArray);
        
        // Calculate average volume
        let sum = 0;
        for (let i = 0; i < bufferLength; i++) {
          sum += dataArray[i];
        }
        const average = sum / bufferLength;
        const percentage = Math.min(100, (average / 128) * 100);
        
        // Update UI
        const fillElement = document.getElementById('micLevelFill');
        const textElement = document.getElementById('micLevelText');
        
        if (fillElement && textElement) {
          fillElement.style.width = percentage + '%';
          textElement.textContent = Math.round(percentage) + '%';
        }
        
        requestAnimationFrame(updateLevel);
      };
      
      updateLevel();
    })
    .catch(err => {
      console.error('Error accessing microphone for level monitoring:', err);
    });
};

VoiceAccessibility.prototype.stopMicLevelMonitoring = function() {
  // Mic level monitoring stops automatically when isEnabled is false
};
