from flask import Flask
import json
import datetime
import os

app = Flask(__name__)
port = int(os.getenv('PORT', '3000'))

@app.route('/')
def root_endpoint():
	return ('CCP2 - Devops 1 Lab Demonstration Service!')

@app.route('/status')
def status():
	return (json.dumps({'status': 'OK'}))

@app.route('/hello/<user>')
def hello(user):
	now = datetime.datetime.now()
	welcome_string = 'Hello '+str(user) + ' - today is ' + datetime.datetime.strftime(now, "%d %b")
	return (json.dumps({'welcome_string': welcome_string}))

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=port)
