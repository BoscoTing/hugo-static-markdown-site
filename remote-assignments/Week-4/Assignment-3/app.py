from flask import Flask, render_template, request, url_for, redirect
from flask_bcrypt import generate_password_hash, check_password_hash
from forms import sign_up, validate_email, select_password, select_email

app = Flask(__name__)

@app.route('/')
def homePage():
    return render_template('index.html')

@app.route('/member_page')
def memberPage():
    return render_template('members.html')

@app.route('/signup_info', 
           methods=["GET"])
def signUpInfo():
    user_info = request.args.get('sign_up')
    user_email = user_info.split(' ')[0]
    user_password = generate_password_hash(user_info.split(' ')[1])
    user_check_password = user_info.split(' ')[2]
    print(user_email, user_password)
    # 信箱是否符合格式、信箱是否仍未註冊
    if validate_email(user_email) == True:
        if user_info.split(' ')[1] == user_check_password:
            try:
                sign_up(user_email, user_password)
                print("Sign up")
                return "Sign up"
            except ValueError:
                return 'registered'
        elif user_info.split(' ')[1] != user_check_password:
            print("Incorrect check_password")
            return "Incorrect check_password"
    else:
        print('invalid email address.')
        return 'Invalid email'

@app.route('/signin_info', 
           methods=["GET"])
def signInInfo():
    user_info = request.args.get('sign_in')
    user_email = user_info.split(' ')[0]
    user_password = user_info.split(' ')[1]
    print(user_email, user_password)
    # 信箱是否符合格式、帳密是否打對
    if validate_email(user_email) == True:
        if select_email(user_email) == True:
            print("correct email")
            if check_password_hash(select_password(user_email), user_password) == True:
                print("Sign in")
                return "Sign in"
            else: 
                return 'Incorrect email or password'
        else:
            return 'Incorrect email or password'
    else:
        print('invalid email address.')
        return 'Invalid email'

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000, debug=True)