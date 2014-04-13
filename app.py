from flask import Flask, render_template, redirect, url_for
from flask import request
from melopy import Melopy
from melopy.scales import *
import dataset

app = Flask(__name__)

db = dataset.connect('sqlite:///file.db')

table = db['beeps']

@app.route('/', methods=['GET', 'POST'])
def index():
	if request.method == 'GET':
		return render_template('index.html')
	else:
		name = str(len(table))
		message = request.form['message']
		beep = dict(name=name, message=message)

		scale = filter(lambda s: s[0] != 'F' and s[0] != 'A', major_scale('C2') + major_scale('C3') + major_scale('C4') + major_scale('C5') + major_scale('C6') + major_scale('C7'))
		m = Melopy('static/' + name, tempo=160)
		for c in message.lower():
			ascii = ord(c)
			if (c >= 'A'):
				ascii -= 97
			else:
				ascii -= 11
			m.add_eighth_note(scale[ascii])
		m.render()
		
		table.insert(beep)
		
		return render_template('index.html', beep=beep)

@app.route('/beeps/', methods=['GET'])
def beeps():
    beeps = table.find()
    return render_template('beeps.html', beeps=beeps)
	

app.run(debug=True)