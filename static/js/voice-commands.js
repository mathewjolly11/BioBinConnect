/**
 * Voice Commands Registration
 * Register all voice commands for BioBinConnect navigation and actions
 */

document.addEventListener('DOMContentLoaded', function() {
    // Wait for voice accessibility to be ready
    if (!window.voiceAccessibility) {
        console.warn('Voice Accessibility not initialized');
        return;
    }
    
    const va = window.voiceAccessibility;
    
    // ========== NAVIGATION COMMANDS ==========
    
    // Home/Dashboard
    va.registerCommand('home', () => {
        window.location.href = '/';
    }, 'Go to home page');

    va.registerCommand('go to home', () => {
        window.location.href = '/';
    }, 'Go to home page');

    // ========== GUEST/PUBLIC COMMANDS ==========
    
    va.registerCommand('login', () => {
        window.location.href = '/login/';
    }, 'Go to login page');

    va.registerCommand('go to login', () => {
        window.location.href = '/login/';
    }, 'Go to login page');

    va.registerCommand('register', () => {
        window.location.href = '/signup/';
    }, 'Go to registration page');

    va.registerCommand('go to register', () => {
        window.location.href = '/signup/';
    }, 'Go to registration page');

    va.registerCommand('sign up', () => {
        window.location.href = '/signup/';
    }, 'Go to registration page');

    va.registerCommand('go to sign up', () => {
        window.location.href = '/signup/';
    }, 'Go to registration page');

    va.registerCommand('services', () => {
        window.location.href = '/services/';
    }, 'View services');

    va.registerCommand('go to services', () => {
        window.location.href = '/services/';
    }, 'View services');

    va.registerCommand('how it works', () => {
        window.location.href = '/how-it-works/';
    }, 'See how it works');

    va.registerCommand('go to how it works', () => {
        window.location.href = '/how-it-works/';
    }, 'See how it works');

    va.registerCommand('booking', () => {
        window.location.href = '/booking/';
    }, 'Go to booking page');

    va.registerCommand('go to booking', () => {
        window.location.href = '/booking/';
    }, 'Go to booking page');

    va.registerCommand('faq', () => {
        window.location.href = '/faq/';
    }, 'View frequently asked questions');

    va.registerCommand('go to faq', () => {
        window.location.href = '/faq/';
    }, 'View frequently asked questions');

    va.registerCommand('contact', () => {
        window.location.href = '/contact/';
    }, 'Contact us');

    va.registerCommand('go to contact', () => {
        window.location.href = '/contact/';
    }, 'Contact us');

    va.registerCommand('about', () => {
        window.location.href = '/about/';
    }, 'About BioBinConnect');

    va.registerCommand('about us', () => {
        window.location.href = '/about/';
    }, 'About BioBinConnect');

    va.registerCommand('go to about', () => {
        window.location.href = '/about/';
    }, 'About BioBinConnect');
    
    const goToDashboard = () => {
        // Detect user type and redirect accordingly
        const path = window.location.pathname;
        if (path.includes('household')) {
            window.location.href = '/household/';
        } else if (path.includes('collector')) {
            window.location.href = '/collector/';
        } else if (path.includes('farmer')) {
            window.location.href = '/farmer/';
        } else if (path.includes('compost-manager')) {
            window.location.href = '/compost-manager/';
        } else if (path.includes('admin')) {
            window.location.href = '/admin/';
        }
    };

    va.registerCommand('dashboard', goToDashboard, 'Go to dashboard');
    va.registerCommand('go to dashboard', goToDashboard, 'Go to dashboard');
    
    // ========== HOUSEHOLD COMMANDS ==========
    
    va.registerCommand('request pickup', () => {
        window.location.href = '/household/request-pickup/';
    }, 'Request waste pickup');

    va.registerCommand('go to request pickup', () => {
        window.location.href = '/household/request-pickup/';
    }, 'Request waste pickup');
    
    va.registerCommand('my requests', () => {
        window.location.href = '/household/my-requests/';
    }, 'View my pickup requests');

    va.registerCommand('go to my requests', () => {
        window.location.href = '/household/my-requests/';
    }, 'View my pickup requests');
    
    va.registerCommand('make payment', () => {
        window.location.href = '/household/make-payment/';
    }, 'Make a payment');

    va.registerCommand('go to make payment', () => {
        window.location.href = '/household/make-payment/';
    }, 'Make a payment');

    va.registerCommand('payment history', () => {
        window.location.href = '/household/payment-history/';
    }, 'View payment history');

    va.registerCommand('go to payment history', () => {
        window.location.href = '/household/payment-history/';
    }, 'View payment history');
    
    const viewProfile = () => {
        const path = window.location.pathname;
        if (path.includes('household')) {
            window.location.href = '/household/profile/';
        } else if (path.includes('collector')) {
            window.location.href = '/collector/profile/';
        } else if (path.includes('farmer')) {
            window.location.href = '/farmer/profile/';
        } else if (path.includes('compost-manager')) {
            window.location.href = '/compost-manager/profile/';
        }
    };

    va.registerCommand('my profile', viewProfile, 'View my profile');
    va.registerCommand('go to my profile', viewProfile, 'View my profile');
    
    // ========== COLLECTOR COMMANDS ==========
    
    va.registerCommand('assigned pickups', () => {
        window.location.href = '/collector/assigned-pickups/';
    }, 'View assigned pickups');

    va.registerCommand('go to assigned pickups', () => {
        window.location.href = '/collector/assigned-pickups/';
    }, 'View assigned pickups');
    
    va.registerCommand('log collection', () => {
        // Need ID for specific log, but can go to list or dashboard
         window.location.href = '/collector/dashboard/';
         va.speak('Please select a pickup from the dashboard to log collection');
    }, 'Log a collection');

    va.registerCommand('history', () => {
        window.location.href = '/collector/history/';
    }, 'View collection history');

    va.registerCommand('go to history', () => {
        window.location.href = '/collector/history/';
    }, 'View collection history');
    
    va.registerCommand('waste inventory', () => {
        window.location.href = '/collector/waste-inventory/';
    }, 'View waste inventory');

    va.registerCommand('go to waste inventory', () => {
        window.location.href = '/collector/waste-inventory/';
    }, 'View waste inventory');
    
    va.registerCommand('sales orders', () => {
        window.location.href = '/collector/sales-orders/';
    }, 'View sales orders');

    va.registerCommand('go to sales orders', () => {
        window.location.href = '/collector/sales-orders/';
    }, 'View sales orders');
    
    // ========== FARMER COMMANDS ==========
    
    va.registerCommand('browse waste', () => {
        window.location.href = '/farmer/browse-waste/';
    }, 'Browse available waste');

    va.registerCommand('go to browse waste', () => {
        window.location.href = '/farmer/browse-waste/';
    }, 'Browse available waste');
    
    va.registerCommand('browse compost', () => {
        window.location.href = '/farmer/browse-compost/';
    }, 'Browse available compost');

    va.registerCommand('go to browse compost', () => {
        window.location.href = '/farmer/browse-compost/';
    }, 'Browse available compost');
    
    va.registerCommand('my orders', () => {
        window.location.href = '/farmer/orders/'; // Fixed path
    }, 'View my orders');

    va.registerCommand('go to my orders', () => {
        window.location.href = '/farmer/orders/'; // Fixed path
    }, 'View my orders');
    
    va.registerCommand('place order', () => {
        window.location.href = '/farmer/place-order/';
    }, 'Place a new order');

    va.registerCommand('go to place order', () => {
        window.location.href = '/farmer/place-order/';
    }, 'Place a new order');
    
    va.registerCommand('payment', () => {
        window.location.href = '/farmer/payment/';
    }, 'Make payment');

    va.registerCommand('go to payment', () => {
        window.location.href = '/farmer/payment/';
    }, 'Make payment');
    
    // ========== COMPOST MANAGER COMMANDS ==========
    
    va.registerCommand('create batch', () => {
        window.location.href = '/compost-manager/create-batch/';
    }, 'Create compost batch');

    va.registerCommand('go to create batch', () => {
        window.location.href = '/compost-manager/create-batch/';
    }, 'Create compost batch');
    
    va.registerCommand('my batches', () => {
        window.location.href = '/compost-manager/my-batches/';
    }, 'View my batches');

    va.registerCommand('go to my batches', () => {
        window.location.href = '/compost-manager/my-batches/';
    }, 'View my batches');

    va.registerCommand('stock management', () => {
        window.location.href = '/compost-manager/stock-management/';
    }, 'Manage stock');

    va.registerCommand('go to stock management', () => {
        window.location.href = '/compost-manager/stock-management/';
    }, 'Manage stock');
    
    // ========== ADMIN COMMANDS ==========
    
    va.registerCommand('manage users', () => {
        window.location.href = '/admin/view-users/';
    }, 'Manage users');

    va.registerCommand('go to manage users', () => {
        window.location.href = '/admin/view-users/';
    }, 'Manage users');
    
    va.registerCommand('waste sales', () => {
        window.location.href = '/admin/waste-sales/';
    }, 'View waste sales');

    va.registerCommand('go to waste sales', () => {
        window.location.href = '/admin/waste-sales/';
    }, 'View waste sales');
    
    va.registerCommand('compost sales', () => {
        window.location.href = '/admin/compost-sales/';
    }, 'View compost sales');

    va.registerCommand('go to compost sales', () => {
        window.location.href = '/admin/compost-sales/';
    }, 'View compost sales');
    
    va.registerCommand('reports', () => {
        window.location.href = '/admin/reports/';
    }, 'View reports');

    va.registerCommand('go to reports', () => {
        window.location.href = '/admin/reports/';
    }, 'View reports');
    
    va.registerCommand('settings', () => {
        window.location.href = '/admin/settings/';
    }, 'System settings');

    va.registerCommand('go to settings', () => {
        window.location.href = '/admin/settings/';
    }, 'System settings');
    
    
    // ========== GENERAL COMMANDS ==========
    
    va.registerCommand('logout', () => {
        if (confirm('Are you sure you want to logout?')) {
            window.location.href = '/logout/';
        }
    }, 'Logout from system');
    
    va.registerCommand('help', () => {
        window.accessibilityToolbar.showVoiceCommandsHelp();
    }, 'Show help and commands');
    
    va.registerCommand('contact', () => {
        const path = window.location.pathname;
        if (path.includes('household')) {
            window.location.href = '/household/contact/';
        } else if (path.includes('collector')) {
            window.location.href = '/collector/contact/';
        } else if (path.includes('farmer')) {
            window.location.href = '/farmer/contact/';
        } else {
            window.location.href = '/contact/'; // Guest/Fallback
        }
    }, 'Contact us');

    va.registerCommand('go to contact', () => {
        // Trying to catch meaningful contact pages based on user logic or general
         const path = window.location.pathname;
        if (path.includes('household')) {
             window.location.href = '/household/contact/';
        } else if (path.includes('collector')) {
             window.location.href = '/collector/contact/';
        } else if (path.includes('farmer')) {
             window.location.href = '/farmer/contact/';
        } else {
             window.location.href = '/contact/'; // Guest/Fallback
        }
    }, 'Contact us');
    
    // ========== PAGE ACTIONS ==========
    
    va.registerCommand('scroll up', () => {
        window.scrollTo({ top: 0, behavior: 'smooth' });
    }, 'Scroll to top of page');
    
    va.registerCommand('scroll down', () => {
        window.scrollTo({ top: document.body.scrollHeight, behavior: 'smooth' });
    }, 'Scroll to bottom of page');
    
    va.registerCommand('go back', () => {
        window.history.back();
    }, 'Go to previous page');
    
    va.registerCommand('refresh', () => {
        window.location.reload();
    }, 'Refresh current page');
    
    // ========== FORM ACTIONS ==========
    
    va.registerCommand('submit form', () => {
        const form = document.querySelector('form');
        if (form) {
            form.submit();
        } else {
            va.speak('No form found on this page');
        }
    }, 'Submit the current form');
    
    va.registerCommand('clear form', () => {
        const form = document.querySelector('form');
        if (form) {
            form.reset();
            va.speak('Form cleared');
        } else {
            va.speak('No form found on this page');
        }
    }, 'Clear all form fields');
    
    // ========== ACCESSIBILITY COMMANDS ==========
    
    va.registerCommand('read page', () => {
        va.readPageContent();
    }, 'Read page content aloud');
    
    va.registerCommand('stop reading', () => {
        va.stopSpeaking();
    }, 'Stop reading content');
    
    va.registerCommand('increase speed', () => {
        const newRate = Math.min(2.0, va.speechRate + 0.2);
        va.setSpeechRate(newRate);
        document.getElementById('speechRate').value = newRate;
        document.getElementById('speechRateValue').textContent = newRate.toFixed(1) + 'x';
        va.speak('Speed increased');
    }, 'Increase reading speed');
    
    va.registerCommand('decrease speed', () => {
        const newRate = Math.max(0.5, va.speechRate - 0.2);
        va.setSpeechRate(newRate);
        document.getElementById('speechRate').value = newRate;
        document.getElementById('speechRateValue').textContent = newRate.toFixed(1) + 'x';
        va.speak('Speed decreased');
    }, 'Decrease reading speed');
    
    console.log('✅ Voice commands registered successfully');
    console.log('Total commands:', Object.keys(va.voiceCommands).length);
});
