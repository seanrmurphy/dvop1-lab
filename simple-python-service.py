#!/usr/bin/python

from flask import Flask
import json
import datetime

app = Flask(__name__)

@app.route('/status')
def status():
	return (json.dumps({'status': 'OK'}))

@app.route('/hello/<user>')
def hello(user):
	now = datetime.datetime.now()
	welcome_string = 'Hello '+str(user) + ' - today is ' + datetime.datetime.strftime(now, "%d %b")
	return (json.dumps({'welcome_string': welcome_string}))

if __name__ == '__main__':
	app.run('localhost', port=8080)
