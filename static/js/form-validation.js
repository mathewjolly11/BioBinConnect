/**
 * BioBinConnect Form Validation System
 * Provides comprehensive validation for all user forms with real-time feedback
 */

class BioBinValidation {
  constructor() {
    this.init();
  }

  init() {
    this.setupFormValidation();
    this.setupHouseNumberValidation();
    this.setupRealTimeValidation();
    this.setupPasswordValidation();
    this.setupPasswordToggle();
    this.addValidationStyles();
  }

  // Add custom CSS styles for validation
  addValidationStyles() {
    const style = document.createElement("style");
    style.textContent = `
            .validation-error {
                border-color: #e74c3c !important;
                box-shadow: 0 0 0 0.2rem rgba(231, 76, 60, 0.25) !important;
            }
            
            .validation-success {
                border-color: #27ae60 !important;
                box-shadow: 0 0 0 0.2rem rgba(39, 174, 96, 0.25) !important;
            }
            
            .error-message {
                color: #e74c3c;
                font-size: 0.875rem;
                margin-top: 0.25rem;
                display: block;
            }
            
            .success-message {
                color: #27ae60;
                font-size: 0.875rem;
                margin-top: 0.25rem;
                display: block;
            }
            
            .validation-spinner {
                width: 16px;
                height: 16px;
                border: 2px solid #f3f3f3;
                border-top: 2px solid #3498db;
                border-radius: 50%;
                animation: spin 1s linear infinite;
                display: inline-block;
                margin-left: 8px;
            }
            
            @keyframes spin {
                0% { transform: rotate(0deg); }
                100% { transform: rotate(360deg); }
            }
            
            .password-strength {
                height: 4px;
                background-color: #f1f1f1;
                border-radius: 2px;
                margin-top: 5px;
                overflow: hidden;
            }
            
            .password-strength-bar {
                height: 100%;
                transition: all 0.3s ease;
                border-radius: 2px;
            }
            
            .strength-weak { background-color: #e74c3c; width: 25%; }
            .strength-fair { background-color: #f39c12; width: 50%; }
            .strength-good { background-color: #f1c40f; width: 75%; }
            .strength-strong { background-color: #27ae60; width: 100%; }
            
            .password-container {
                position: relative;
                display: flex;
                align-items: center;
                width: 100%;
            }
            
            .password-toggle {
                position: absolute;
                right: 8px;
                top: 50%;
                transform: translateY(-50%);
                background: rgba(255, 255, 255, 0.9);
                border: 1px solid #ddd;
                cursor: pointer;
                color: #6c9a2e;
                font-size: 18px;
                z-index: 100;
                padding: 6px;
                display: flex;
                align-items: center;
                justify-content: center;
                width: 32px;
                height: 32px;
                border-radius: 6px;
                transition: all 0.3s ease;
                box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
            }
            
            .password-toggle:hover {
                background-color: #6c9a2e;
                color: white;
                border-color: #6c9a2e;
                transform: translateY(-50%) scale(1.05);
                box-shadow: 0 3px 8px rgba(108, 154, 46, 0.3);
            }
            
            .password-toggle:active {
                transform: translateY(-50%) scale(0.95);
            }
            
            .password-toggle i {
                pointer-events: none;
                transition: all 0.2s ease;
                font-size: 16px;
                display: flex;
                align-items: center;
                justify-content: center;
                font-style: normal;
            }
            
            /* Show emoji fallback when BoxIcons don't load */
            .password-toggle i:empty:after {
                content: '👁';
                font-size: 16px;
            }
            
            .password-container input[type="password"],
            .password-container input[type="text"] {
                width: 100%;
                padding-right: 48px !important;
            }
            
            /* Position validation messages below password fields */
            .password-container + .error-message,
            .password-container + .success-message,
            .password-container + .validation-message {
                margin-top: 8px;
                display: block;
                position: relative;
                z-index: 1;
            }
            
            /* Position validation messages below all input fields */
            .error-message,
            .success-message,
            .validation-message {
                display: block;
                margin-top: 8px;
                margin-bottom: 8px;
                padding: 6px 12px;
                border-radius: 4px;
                font-size: 14px;
                line-height: 1.4;
                clear: both;
                width: 100%;
                position: relative;
                z-index: 1;
            }
            
            .error-message {
                background-color: #fee;
                color: #c33;
                border: 1px solid #fcc;
            }
            
            .success-message {
                background-color: #efe;
                color: #6c9a2e;
                border: 1px solid #6c9a2e;
            }
            
            /* Ensure form fields have proper spacing */
            .form-group,
            .password-container {
                margin-bottom: 20px;
                position: relative;
            }
            
            /* Enhanced validation message styles - force visibility */
            .error-message {
                color: #e74c3c !important;
                font-size: 14px !important;
                margin-top: 8px !important;
                margin-bottom: 8px !important;
                padding: 8px 12px !important;
                background-color: #fee !important;
                border: 1px solid #fcc !important;
                border-radius: 4px !important;
                display: block !important;
                width: 100% !important;
                box-sizing: border-box !important;
                clear: both !important;
            }
            
            .success-message {
                color: #6c9a2e !important;
                font-size: 14px !important;
                margin-top: 8px !important;
                margin-bottom: 8px !important;
                padding: 8px 12px !important;
                background-color: #efe !important;
                border: 1px solid #6c9a2e !important;
                border-radius: 4px !important;
                display: block !important;
                width: 100% !important;
                box-sizing: border-box !important;
                clear: both !important;
            }
            
            .validation-message {
                color: #856404 !important;
                font-size: 14px !important;
                margin-top: 8px !important;
                margin-bottom: 8px !important;
                padding: 8px 12px !important;
                background-color: #fff3cd !important;
                border: 1px solid #ffeaa7 !important;
                border-radius: 4px !important;
                display: block !important;
                width: 100% !important;
                box-sizing: border-box !important;
                clear: both !important;
            }
        `;
    document.head.appendChild(style);
  }

  // Setup general form validation
  setupFormValidation() {
    // Email validation
    this.setupEmailValidation();

    // Phone validation
    this.setupPhoneValidation();

    // Name validation
    this.setupNameValidation();

    // Number validation
    this.setupNumberValidation();

    // File validation
    this.setupFileValidation();
  }

  setupEmailValidation() {
    const emailInputs = document.querySelectorAll(
      'input[type="email"], input[placeholder*="email"], input[placeholder*="Email"]'
    );

    emailInputs.forEach((input) => {
      input.addEventListener("input", (e) => {
        this.validateEmail(e.target);
      });

      input.addEventListener("blur", (e) => {
        this.validateEmail(e.target);
      });
    });
  }

  validateEmail(input) {
    const email = input.value.trim();
    const emailRegex = /^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/;

    this.clearValidationMessage(input);

    if (!email) {
      this.showValidationError(input, "Email is required");
      return false;
    }

    if (!emailRegex.test(email)) {
      this.showValidationError(input, "Please enter a valid email address");
      return false;
    }

    this.showValidationSuccess(input, "Email format is valid");
    return true;
  }

  setupPhoneValidation() {
    const phoneInputs = document.querySelectorAll(
      'input[placeholder*="phone"], input[placeholder*="Phone"], input[placeholder*="mobile"], input[placeholder*="Mobile"]'
    );

    phoneInputs.forEach((input) => {
      // Auto-format phone number as user types
      input.addEventListener("input", (e) => {
        let value = e.target.value.replace(/\D/g, ""); // Remove non-digits
        if (value.length > 10) {
          value = value.slice(0, 10); // Limit to 10 digits
        }
        e.target.value = value;
        this.validatePhone(e.target);
      });

      input.addEventListener("blur", (e) => {
        this.validatePhone(e.target);
      });
    });
  }

  validatePhone(input) {
    const phone = input.value.trim();
    const phoneRegex = /^[0-9]{10}$/;

    this.clearValidationMessage(input);

    if (!phone) {
      this.showValidationError(input, "Phone number is required");
      return false;
    }

    if (!phoneRegex.test(phone)) {
      this.showValidationError(input, "Phone number must be exactly 10 digits");
      return false;
    }

    if (phone.charAt(0) < "6") {
      this.showValidationError(
        input,
        "Phone number should start with 6, 7, 8, or 9"
      );
      return false;
    }

    this.showValidationSuccess(input, "Phone number is valid");
    return true;
  }

  setupNameValidation() {
    const nameInputs = document.querySelectorAll(
      'input[placeholder*="name"], input[placeholder*="Name"]'
    );

    nameInputs.forEach((input) => {
      input.addEventListener("input", (e) => {
        this.validateName(e.target);
      });

      input.addEventListener("blur", (e) => {
        this.validateName(e.target);
      });
    });
  }

  validateName(input) {
    const name = input.value.trim();
    const nameRegex = /^[a-zA-Z\s]+$/;

    this.clearValidationMessage(input);

    if (!name) {
      this.showValidationError(input, "Name is required");
      return false;
    }

    if (name.length < 2) {
      this.showValidationError(input, "Name must be at least 2 characters");
      return false;
    }

    if (!nameRegex.test(name)) {
      this.showValidationError(
        input,
        "Name should only contain letters and spaces"
      );
      return false;
    }

    this.showValidationSuccess(input, "Name is valid");
    return true;
  }

  setupNumberValidation() {
    const numberInputs = document.querySelectorAll(
      'input[type="number"]:not(.house-number-input)'
    );

    numberInputs.forEach((input) => {
      input.addEventListener("input", (e) => {
        this.validateNumber(e.target);
      });

      input.addEventListener("blur", (e) => {
        this.validateNumber(e.target);
      });
    });
  }

  validateNumber(input) {
    const value = parseFloat(input.value);
    const min = parseFloat(input.getAttribute("min"));
    const max = parseFloat(input.getAttribute("max"));

    this.clearValidationMessage(input);

    if (isNaN(value) || input.value.trim() === "") {
      this.showValidationError(input, "Please enter a valid number");
      return false;
    }

    if (!isNaN(min) && value < min) {
      this.showValidationError(input, `Value must be at least ${min}`);
      return false;
    }

    if (!isNaN(max) && value > max) {
      this.showValidationError(input, `Value must not exceed ${max}`);
      return false;
    }

    this.showValidationSuccess(input, "Number is valid");
    return true;
  }

  setupFileValidation() {
    const fileInputs = document.querySelectorAll('input[type="file"]');

    fileInputs.forEach((input) => {
      input.addEventListener("change", (e) => {
        this.validateFile(e.target);
      });
    });
  }

  validateFile(input) {
    const file = input.files[0];
    const maxSize = 5 * 1024 * 1024; // 5MB
    const allowedTypes = [
      "image/jpeg",
      "image/jpg",
      "image/png",
      "image/gif",
      "image/webp",
      "image/avif",
    ];

    this.clearValidationMessage(input);

    if (!file) {
      return true; // File might not be required
    }

    if (file.size > maxSize) {
      this.showValidationError(input, "File size must be less than 5MB");
      return false;
    }

    if (!allowedTypes.includes(file.type)) {
      this.showValidationError(
        input,
        "Please select a valid image file (JPEG, PNG, GIF, WebP, AVIF)"
      );
      return false;
    }

    this.showValidationSuccess(input, "File is valid");
    return true;
  }

  // House number validation with live checking
  setupHouseNumberValidation() {
    const houseInputs = document.querySelectorAll(
      '.house-number-input, input[data-validate-house="true"]'
    );

    houseInputs.forEach((input) => {
      // Only validate when user finishes entering (on blur)
      input.addEventListener("blur", (e) => {
        const value = e.target.value.trim();
        if (value) {
          this.validateHouseNumber(input);
        }
      });

      // Clear validation message when user starts typing again
      input.addEventListener("input", (e) => {
        this.clearValidationMessage(input);
      });
    });
  }

  async validateHouseNumber(input) {
    const houseNo = input.value.trim();

    this.clearValidationMessage(input);

    if (!houseNo) {
      this.showValidationError(input, "House number is required");
      return false;
    }

    const houseNum = parseInt(houseNo);
    if (isNaN(houseNum) || houseNum < 1) {
      this.showValidationError(input, "House number must be a positive number");
      return false;
    }

    // Get form context for validation
    const form = input.closest("form");
    const districtSelect = form.querySelector('select[name*="district"]');
    const locationSelect = form.querySelector('select[name*="location"]');
    const raSelect = form.querySelector(
      'select[name*="residents_association"]'
    );

    const data = {
      house_no: houseNum,
      district_id: districtSelect ? districtSelect.value : null,
      location_id: locationSelect ? locationSelect.value : null,
    residents_association_id: raSelect ? raSelect.value : null,
      current_household_id:
        form.querySelector('input[name="current_household_id"]')?.value || null,
    };

    try {
      const response = await fetch("/api/validate-house-number/", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
          "X-CSRFToken": this.getCsrfToken(),
        },
        body: JSON.stringify(data),
      });

      const result = await response.json();

      if (result.valid) {
        this.showValidationSuccess(input, result.message);
        return true;
      } else {
        let errorMessage = result.message;
        if (result.suggestion) {
          errorMessage += ` <button type="button" class="btn btn-sm btn-outline-primary ml-2" onclick="this.parentElement.previousElementSibling.value='${result.suggestion}'; window.bioBinValidation.validateHouseNumber(this.parentElement.previousElementSibling);">Use ${result.suggestion}</button>`;
        }
        this.showValidationError(input, errorMessage, true);
        return false;
      }
    } catch (error) {
      console.error("House number validation error:", error);
      this.showValidationError(
        input,
        "Unable to validate house number. Please try again."
      );
      return false;
    }
  }

  // Password visibility toggle
  setupPasswordToggle() {
    const passwordInputs = document.querySelectorAll('input[type="password"]');

    passwordInputs.forEach((input) => {
      // Skip if already processed
      if (!input.hasAttribute("data-toggle-added")) {
        this.createPasswordToggle(input);
      }
    });
  }

  createPasswordToggle(input) {
    // Skip if already processed
    if (input.hasAttribute("data-toggle-added")) {
      return;
    }

    // Skip if already has toggle
    if (input.parentElement.classList.contains("password-container")) {
      return;
    }

    // Mark as processed immediately
    input.setAttribute("data-toggle-added", "true");

    // Create container
    const container = document.createElement("div");
    container.className = "password-container";

    // Wrap input in container
    input.parentNode.insertBefore(container, input);
    container.appendChild(input);

    // Create toggle button
    const toggleBtn = document.createElement("button");
    toggleBtn.type = "button";
    toggleBtn.className = "password-toggle";
    toggleBtn.innerHTML = "👁️";
    toggleBtn.title = "Click to show password";

    // Add click event
    toggleBtn.addEventListener("click", () => {
      const isPassword = input.type === "password";
      input.type = isPassword ? "text" : "password";
      toggleBtn.innerHTML = isPassword ? "🙈" : "👁️";
      toggleBtn.title = isPassword
        ? "Click to hide password"
        : "Click to show password";
    });

    container.appendChild(toggleBtn);
  }

  // Override showValidationError for password fields to position messages correctly
  showValidationError(input, message, allowHTML = false) {
    input.classList.remove("validation-success");
    input.classList.add("validation-error");

    // Always clear existing messages first
    this.clearValidationMessage(input);

    // Only create one message
    const errorDiv = document.createElement("div");
    errorDiv.className = "error-message";
    if (allowHTML) {
      errorDiv.innerHTML = message;
    } else {
      errorDiv.textContent = message;
    }

    // For password fields, insert after the container
    const container = input.closest(".password-container");
    if (container) {
      container.parentNode.insertBefore(errorDiv, container.nextSibling);
    } else {
      // For regular input fields, insert after the input
      input.parentNode.insertBefore(errorDiv, input.nextSibling);
    }
  }

  showValidationSuccess(input, message) {
    input.classList.remove("validation-error");
    input.classList.add("validation-success");

    this.clearValidationMessage(input);

    if (message) {
      const successDiv = document.createElement("div");
      successDiv.className = "success-message";
      successDiv.textContent = message;

      // For password fields, insert after the container
      const container = input.closest(".password-container");
      if (container) {
        container.parentNode.insertBefore(successDiv, container.nextSibling);
      } else {
        input.parentNode.appendChild(successDiv);
      }
    }
  }

  clearValidationMessage(input) {
    // For password fields, look for messages after the container
    const container = input.closest(".password-container");
    if (container) {
      let nextElement = container.nextSibling;
      while (
        nextElement &&
        (nextElement.classList?.contains("error-message") ||
          nextElement.classList?.contains("success-message") ||
          nextElement.classList?.contains("validation-message"))
      ) {
        const toRemove = nextElement;
        nextElement = nextElement.nextSibling;
        toRemove.remove();
      }
    } else {
      const messages = input.parentNode.querySelectorAll(
        ".error-message, .success-message, .validation-message"
      );
      messages.forEach((msg) => msg.remove());
    }

    input.classList.remove("validation-error", "validation-success");
  }

  // Password strength validation
  setupPasswordValidation() {
    const passwordInputs = document.querySelectorAll('input[type="password"]');

    passwordInputs.forEach((input) => {
      if (
        input.name === "password1" ||
        (input.placeholder.toLowerCase().includes("password") &&
          !input.placeholder.toLowerCase().includes("confirm"))
      ) {
        this.createPasswordStrengthIndicator(input);

        input.addEventListener("input", (e) => {
          this.validatePasswordStrength(e.target);
        });
      }

      if (
        input.name === "password2" ||
        input.placeholder.toLowerCase().includes("confirm")
      ) {
        input.addEventListener("input", (e) => {
          this.validatePasswordConfirm(e.target);
        });
      }
    });
  }

  createPasswordStrengthIndicator(input) {
    const strengthIndicator = document.createElement("div");
    strengthIndicator.className = "password-strength";
    const strengthBar = document.createElement("div");
    strengthBar.className = "password-strength-bar";
    strengthIndicator.appendChild(strengthBar);

    input.parentNode.appendChild(strengthIndicator);
    input.strengthBar = strengthBar;
  }

  validatePasswordStrength(input) {
    const password = input.value;
    const minLength = 8;

    this.clearValidationMessage(input);

    if (!password) {
      if (input.strengthBar) {
        input.strengthBar.className = "password-strength-bar";
      }
      return false;
    }

    let strength = 0;
    let messages = [];

    // Length check
    if (password.length >= minLength) strength += 25;
    else messages.push(`At least ${minLength} characters`);

    // Lowercase check
    if (/[a-z]/.test(password)) strength += 25;
    else messages.push("One lowercase letter");

    // Uppercase check
    if (/[A-Z]/.test(password)) strength += 25;
    else messages.push("One uppercase letter");

    // Number check
    if (/[0-9]/.test(password)) strength += 25;
    else messages.push("One number");

    // Update strength bar
    if (input.strengthBar) {
      input.strengthBar.className = "password-strength-bar";
      if (strength >= 75) input.strengthBar.classList.add("strength-strong");
      else if (strength >= 50) input.strengthBar.classList.add("strength-good");
      else if (strength >= 25) input.strengthBar.classList.add("strength-fair");
      else input.strengthBar.classList.add("strength-weak");
    }

    if (strength < 100) {
      this.showValidationError(input, `Password needs: ${messages.join(", ")}`);
      return false;
    }

    this.showValidationSuccess(input, "Strong password");
    return true;
  }

  validatePasswordConfirm(input) {
    const form = input.closest("form");
    const passwordInput =
      form.querySelector('input[name="password1"]') ||
      form.querySelector('input[type="password"]:not([name="password2"])');

    this.clearValidationMessage(input);

    if (!input.value) {
      this.showValidationError(input, "Please confirm your password");
      return false;
    }

    if (!passwordInput || input.value !== passwordInput.value) {
      this.showValidationError(input, "Passwords do not match");
      return false;
    }

    this.showValidationSuccess(input, "Passwords match");
    return true;
  }

  // Real-time validation setup
  setupRealTimeValidation() {
    const forms = document.querySelectorAll("form");

    forms.forEach((form) => {
      form.addEventListener("submit", (e) => {
        // Check if this is a multi-step form navigation button
        const submitter = e.submitter;
        
        // Skip validation for Next/Previous buttons
        if (submitter && (
          submitter.classList.contains('next-step') || 
          submitter.classList.contains('prev-step') ||
          submitter.type === 'button'
        )) {
          return; // Don't validate, allow navigation
        }
        
        // Only validate on actual form submission
        if (!this.validateForm(form)) {
          e.preventDefault();
          this.showFormErrors(form);
        }
      });

      // Add Bootstrap validation classes
      form.classList.add("needs-validation");
      form.setAttribute("novalidate", "");
    });
  }

  validateForm(form) {
    const inputs = form.querySelectorAll(
      "input[required], textarea[required], select[required]"
    );
    let isValid = true;

    inputs.forEach((input) => {
      // Skip validation for hidden fields (from inactive steps)
      if (input.offsetParent === null || 
          input.style.display === 'none' ||
          input.closest('.register-step:not(.active)') ||
          input.closest('[style*="display: none"]')) {
        return; // Skip this field
      }
      
      let fieldValid = false;

      if (input.type === "email") {
        fieldValid = this.validateEmail(input);
      } else if (
        input.getAttribute("placeholder")?.toLowerCase().includes("phone") ||
        input.getAttribute("placeholder")?.toLowerCase().includes("mobile")
      ) {
        fieldValid = this.validatePhone(input);
      } else if (
        input.getAttribute("placeholder")?.toLowerCase().includes("name")
      ) {
        fieldValid = this.validateName(input);
      } else if (input.type === "number") {
        fieldValid = this.validateNumber(input);
      } else if (input.type === "file") {
        fieldValid = this.validateFile(input);
      } else if (input.type === "password") {
        if (input.name === "password1" || !input.name.includes("2")) {
          fieldValid = this.validatePasswordStrength(input);
        } else {
          fieldValid = this.validatePasswordConfirm(input);
        }
      } else {
        // Generic required field validation
        if (!input.value.trim()) {
          this.showValidationError(input, "This field is required");
          fieldValid = false;
        } else {
          this.showValidationSuccess(input, "");
          fieldValid = true;
        }
      }

      if (!fieldValid) isValid = false;
    });

    return isValid;
  }

  showFormErrors(form) {
    const firstError = form.querySelector(".validation-error");
    if (firstError) {
      firstError.focus();
      firstError.scrollIntoView({ behavior: "smooth", block: "center" });
    }

    // Show a toast/alert for form errors
    if (window.Swal) {
      Swal.fire({
        title: "Form Validation Error",
        text: "Please correct the highlighted errors and try again.",
        icon: "error",
        confirmButtonText: "OK",
        confirmButtonColor: "#e74c3c",
      });
    } else {
      alert("Please correct the form errors and try again.");
    }
  }

  // Utility methods
  showValidationError(input, message, allowHTML = false) {
    input.classList.remove("validation-success");
    input.classList.add("validation-error");

    // Always clear existing messages first
    this.clearValidationMessage(input);

    const errorDiv = document.createElement("div");
    errorDiv.className = "error-message";
    if (allowHTML) {
      errorDiv.innerHTML = message;
    } else {
      errorDiv.textContent = message;
    }

    // Position correctly for password and regular fields
    const container = input.closest(".password-container");
    if (container) {
      container.parentNode.insertBefore(errorDiv, container.nextSibling);
    } else {
      input.parentNode.insertBefore(errorDiv, input.nextSibling);
    }
  }

  showValidationSuccess(input, message, allowHTML = false) {
    input.classList.remove("validation-error");
    input.classList.add("validation-success");

    this.clearValidationMessage(input);

    if (message && message.trim()) {
      const successDiv = document.createElement("div");
      successDiv.className = "success-message";
      if (allowHTML) {
        successDiv.innerHTML = message;
      } else {
        successDiv.textContent = message;
      }

      // For password fields, insert after the container
      const container = input.closest(".password-container");
      if (container) {
        container.parentNode.insertBefore(successDiv, container.nextSibling);
      } else {
        // For regular input fields, insert after the input
        input.parentNode.insertBefore(successDiv, input.nextSibling);
      }
    }
  }

  showValidationSpinner(input) {
    this.clearValidationMessage(input);

    const spinnerDiv = document.createElement("div");
    spinnerDiv.className = "validation-message";
    spinnerDiv.innerHTML =
      'Checking availability <span class="validation-spinner"></span>';

    // For password fields, insert after the container
    const container = input.closest(".password-container");
    if (container) {
      container.parentNode.insertBefore(spinnerDiv, container.nextSibling);
    } else {
      input.parentNode.appendChild(spinnerDiv);
    }
  }

  clearValidationMessage(input) {
    // Check if input is in a password container
    const container = input.closest(".password-container");

    if (container) {
      // For password fields, look for messages after the container
      let nextElement = container.nextSibling;
      while (
        nextElement &&
        nextElement.nodeType === 1 &&
        (nextElement.classList.contains("error-message") ||
          nextElement.classList.contains("success-message") ||
          nextElement.classList.contains("validation-message"))
      ) {
        const toRemove = nextElement;
        nextElement = nextElement.nextSibling;
        toRemove.remove();
      }
    } else {
      // For regular fields, look in parent and siblings
      let nextElement = input.nextSibling;
      while (
        nextElement &&
        nextElement.nodeType === 1 &&
        (nextElement.classList.contains("error-message") ||
          nextElement.classList.contains("success-message") ||
          nextElement.classList.contains("validation-message"))
      ) {
        const toRemove = nextElement;
        nextElement = nextElement.nextSibling;
        toRemove.remove();
      }

      // Also check parent for any orphaned messages
      const parent = input.parentNode;
      const orphanedMessages = parent.querySelectorAll(
        ".error-message, .success-message, .validation-message"
      );
      orphanedMessages.forEach((msg) => {
        // Only remove if it's not attached to another input
        if (
          !msg.previousElementSibling ||
          msg.previousElementSibling === input ||
          msg.previousElementSibling.classList.contains("password-container")
        ) {
          msg.remove();
        }
      });
    }

    input.classList.remove("validation-error", "validation-success");
  }

  getCsrfToken() {
    const cookieValue = document.cookie
      .split("; ")
      .find((row) => row.startsWith("csrftoken="))
      ?.split("=")[1];
    return (
      cookieValue ||
      document.querySelector("[name=csrfmiddlewaretoken]")?.value ||
      ""
    );
  }
}

// Initialize validation when DOM is loaded
if (typeof window.bioBinValidation === "undefined") {
  document.addEventListener("DOMContentLoaded", function () {
    window.bioBinValidation = new BioBinValidation();
  });

  // Handle case where DOM is already loaded
  if (
    document.readyState === "complete" ||
    document.readyState === "interactive"
  ) {
    setTimeout(() => {
      if (!window.bioBinValidation) {
        window.bioBinValidation = new BioBinValidation();
      }
    }, 100);
  }
}

// Utility function for manual validation calls
function validateField(input) {
  if (window.bioBinValidation) {
    window.bioBinValidation.validateField(input);
  }
}

// Utility function to manually initialize password toggles
function initializePasswordToggles() {
  if (window.bioBinValidation) {
    window.bioBinValidation.setupPasswordToggle();
  }
}
