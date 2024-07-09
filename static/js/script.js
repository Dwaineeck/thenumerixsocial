document.addEventListener('DOMContentLoaded', function () {
    const toggleButton = document.getElementById('toggle-button');
    const authButton = document.getElementById('auth-button');
    const formTitle = document.getElementById('form-title');
    const emailGroup = document.getElementById('email-group');
    const authForm = document.getElementById('auth-form');

    toggleButton.addEventListener('click', function () {
        if (authButton.textContent === 'Login') {
            authButton.textContent = 'Sign Up';
            formTitle.innerHTML = '<img src="/static/logo.png" width="30" height="30" class="d-inline-block align-top" alt="thenumerix logo" loading="lazy"> Sign Up';
            emailGroup.style.display = 'block';
            toggleButton.textContent = 'Login';
        } else {
            authButton.textContent = 'Login';
            formTitle.innerHTML = '<img src="/static/logo.png" width="30" height="30" class="d-inline-block align-top" alt="thenumerix logo" loading="lazy"> Login';
            emailGroup.style.display = 'none';
            toggleButton.textContent = 'Sign Up';
        }
    });

    authForm.addEventListener('submit', function (e) {
        e.preventDefault();
        // Add your form submission logic here
    });
});
document.addEventListener('DOMContentLoaded', function () {
    const signupForm = document.getElementById('signupForm');
    if (signupForm) {
        signupForm.addEventListener('submit', function (e) {
            e.preventDefault();
            const formData = new FormData(signupForm);
            fetch(signupForm.action, {
                method: 'POST',
                body: formData,
                headers: {
                    'X-Requested-With': 'XMLHttpRequest',
                },
            })
            .then(response => response.json())
            .then(data => {
                if (data.success) {
                    window.location.href = '/newpage/';
                } else {
                    // Handle error
                }
            })
            .catch(error => console.error('Error:', error));
        });
    }
});
