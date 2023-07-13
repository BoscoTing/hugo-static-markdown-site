from flask import (Flask, render_template, 
                   redirect, url_for, 
                   request, send_from_directory)

app = Flask(__name__)

@app.route('/')
def index():
		return render_template('index.html')

@app.route('/data', methods = ['GET'])
def series( ):
    number = request.args.get('number')
    if number == "" or number == None:
        return '<p>Lack of Parameter</p>'
    elif (int(float(number)) < 0) or ( (float(number)).is_integer()==False ):
        return "<p>Number should be a positive integer!</p>"
    else:
        sum = 0
        for i in range(1, int(number)+1):
            sum += i 
        return f'<p>{sum}</p>'
    
@app.route('/sum.html')
def sum_page():
      return app.send_static_file('sum.html')

if __name__ == "__main__":
    app.run(port=3000, debug=True)