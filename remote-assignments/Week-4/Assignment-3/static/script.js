//  註冊
var signUpButton = document.getElementById('sign_up_botton')
signUpButton.addEventListener('click', () => {
    let userEmail = document.getElementById('user_signup_email').value;
    let userPassword = document.getElementById('user_signup_password').value;
    let userCheckPassword = document.getElementById('user_signup_check_password').value;

    
    var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function () {
        if (this.readyState === 4 && this.status === 200) {
            if (this.response === 'registered') {
                alert('This mail have been registerd.')
            }   
            if (this.response === 'Invalid email') {
                alert('Invalid email address.')
            }
            if (this.response === 'Incorrect check_password') {
                alert('Please recheck your password.')
            }   
            if (this.response === 'Sign up') {
                alert('Sign up successfully.')
                window.location.replace('/member_page')
                }
        }
    };
    xhttp.open("GET", `/signup_info?sign_up=${userEmail} ${userPassword} ${userCheckPassword}`, true);
    xhttp.send();
});

//  登入
var signInButton = document.getElementById('sign_in_botton')
signInButton.addEventListener('click', () => {
    let userEmail = document.getElementById('user_signin_email').value;
    let userPassword = document.getElementById('user_signin_password').value;
    
    var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function () {
        if (this.readyState === 4 && this.status === 200) {
            if (this.response === 'Incorrect email or password') {
                alert('Incorrect email or password.')
            }   
            if (this.response === "Sign in") {
                alert("Sign in successfully.")
                window.location.replace("/member_page")
            }
        }
    };
    xhttp.open("GET", `/signin_info?sign_in=${userEmail} ${userPassword}`, true);
    xhttp.send();
});