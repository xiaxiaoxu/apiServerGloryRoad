from flask import Flask
app = Flask(__name__)

def sayHello():
	print('Hello')

@app.route("/test")
def index():
	return "hello flask"

