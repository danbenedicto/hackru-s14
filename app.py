from flask import Flask, render_template, redirect, url_for
from flask import request
from melopy import Melopy
from melopy.scales import *
import dataset

app = Flask(__name__)

db = dataset.connect('sqlite:///file.db')

table = db['beeps']

@app.route('/', methods=['GET'])
def index():
	return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
	name = request.form['name']
	message = request.form['message']
	beep = dict(name=name, message=message)

	scale = minor_pentatonic_scale('C2') + minor_pentatonic_scale('C3') + minor_pentatonic_scale('C4') + minor_pentatonic_scale('C5') + minor_pentatonic_scale('C6') + minor_pentatonic_scale('C7')
	m = Melopy('static/' + name)
	for c in message.lower():
		m.add_eighth_note(scale[ord(c) - 97])
	m.render()
	
	table.insert(beep)
	
	return redirect(url_for('beeps', name=name))

@app.route('/beeps/<name>', methods=['GET'])
def beeps(name):
    # beeps = table.find()
    return render_template('playback.html', name=name)
	

app.run(debug=True)