#!/usr/bin/env python3

from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return 'Index Page'

@app.route('/hello')
def hello():
    return 'Hello, World'

@app.route('/webdev')
def webdev():
	return render_template('index.html')
