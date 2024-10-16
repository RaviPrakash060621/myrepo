document.addEventListener('DOMContentLoaded', () => {
    const loginLink = document.getElementById('loginLink');
    const registerLink = document.getElementById('registerLink');
    const logoutLink = document.getElementById('logoutLink');
    const authSection = document.getElementById('authSection');

    function showLoginForm() {
        authSection.innerHTML = `
            <h2>Login</h2>
            <form id="loginForm">
                <input type="text" id="loginUsername" placeholder="Username" required>
                <input type="password" id="loginPassword" placeholder="Password" required>
                <button type="submit">Login</button>
            </form>
        `;
    }

    function showRegisterForm() {
        authSection.innerHTML = `
            <h2>Register</h2>
            <form id="registerForm">
                <input type="text" id="registerUsername" placeholder="Username" required>
                <input type="password" id="registerPassword" placeholder="Password" required>
                <button type="submit">Register</button>
            </form>
        `;
    }

    loginLink.addEventListener('click', (e) => {
        e.preventDefault();
        showLoginForm();
    });

    registerLink.addEventListener('click', (e) => {
        e.preventDefault();
        showRegisterForm();
    });

    logoutLink.addEventListener('click', (e) => {
        e.preventDefault();
        // Add logic to handle logout
        authSection.innerHTML = '<h2>Logged out successfully.</h2>';
        logoutLink.style.display = 'none';
        loginLink.style.display = 'inline';
        registerLink.style.display = 'inline';
    });

    // For demo purposes, simulate a logged-in user
    // In a real application, replace this with actual authentication logic
    const isLoggedIn = false; // Change to true to simulate a logged-in state
    if (isLoggedIn) {
        authSection.innerHTML = '<h2>Welcome back!</h2>';
        loginLink.style.display = 'none';
        registerLink.style.display = 'none';
        logoutLink.style.display = 'inline';
    } else {
        showLoginForm();
    }
});
