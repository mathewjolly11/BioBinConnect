const loginRegisterPage = document.querySelector('.login-register-page');
if (loginRegisterPage) {
    const container = loginRegisterPage.querySelector('.container');
    const registerBtn = loginRegisterPage.querySelector('.register-btn');
    const loginBtn = loginRegisterPage.querySelector('.login-btn');

    if (registerBtn && container) {
        registerBtn.addEventListener('click', () => {
            container.classList.add('active');
        });
    }
    if (loginBtn && container) {
        loginBtn.addEventListener('click', () => {
            container.classList.remove('active');
        });
    }
}