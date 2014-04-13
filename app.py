from flask import Flask, redirect, url_for
from flask import request
from melopy import Melopy
from melopy.scales import *

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
	return 'welcome!'

@app.route('/submit', methods=['GET'])
def submit():
	name = request.args.get('text')
	scale = major_scale('C3') + major_scale('C4') + major_scale('C5') + major_scale('C6') + major_scale('C7')
	m = Melopy('newsong')
	for c in name:
		m.add_eighth_note(scale[ord(c) - 90])
	m.render()
	return redirect(url_for('index'))
	

app.run(debug=True)