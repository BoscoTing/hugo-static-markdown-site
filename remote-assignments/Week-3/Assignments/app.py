import json
from flask import (Flask, 
                   render_template, 
                   redirect, 
                   url_for, 
                   request, 
                   send_from_directory,
                   make_response)

app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html')

# 計算級數
@app.route('/data', 
           methods = ['GET'])
def series():
    number = request.args.get('number')
    if number == "" or number == None:
        return '<p>Lack of Parameter</p>'
    elif (( number.isdigit() == False ) or
          ( int(float(number)) < 0 ) or 
          ( (float(number)).is_integer() == False )):
        return "<p>Number should be a positive integer!</p>"
    else:
        sum = 0
        for i in range(1, int(number)+1):
            sum += i 
        return f'<p>{sum}</p>'
    
@app.route('/sum.html')
def sum_page():
    return app.send_static_file('sum.html')

def get_saved_data():
    try:
        data = json.loads(request.cookies.get('user'))
    except TypeError: 
        data = {}
    return data # as a dictionary

@app.route('/myName')
def my_name():
    data = get_saved_data() 
    return render_template('myname.html', saves=data)

@app.route('/trackName', 
           methods = ["POST"])
def track_name():
    if request.method == "POST":
        response = make_response(redirect(url_for('my_name'))) 
        data = get_saved_data()
        data.update(dict(request.form.items())) 
        response.set_cookie('user', 
                            json.dumps(data))
        return response
    
@app.route('/trackName', methods=['GET'])
def track_name_get():
    name = request.args.get('name')
    if name:
        data = json.loads(request.cookies.get('user'))
        data['user'] = name
        response = make_response(redirect(url_for('my_name')))
        response.set_cookie('user', 
                            json.dumps(data))
    return response


if __name__ == "__main__":
    app.run(port=8000, debug=True)