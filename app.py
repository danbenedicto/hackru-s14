from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/', methods=['GET'])
def hello():
	name = request.args.get('name')
	return "sup MY nigga " + name

app.run(debug=True)