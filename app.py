from flask import Flask, render_template
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
	scale = minor_pentatonic_scale('C2') + minor_pentatonic_scale('C3') + minor_pentatonic_scale('C4') + minor_pentatonic_scale('C5') + minor_pentatonic_scale('C6') + minor_pentatonic_scale('C7')
	m = Melopy('newsong')
	for c in name.lower():
		m.add_eighth_note(scale[ord(c) - 97])
	m.render()
	return render_template('playback.html', name='mysong')
	

app.run(debug=True)