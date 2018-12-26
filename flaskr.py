from flask import Flask, request, render_template
from algorithm import Prime  

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def index_post():
    text = request.form['number']

    if not text:
	    return "please enter an intger"

    if not text.isdigit() :
    	return "the number should be an intger and greater than 1"

    number= int(text)
    if number<=1 :
    	return "the number should be an intger and greater than 1"

    if Prime( int(number) ).check():
        return text + " is prime number"
    else:
        return text + " is composite number"


