#!/usr/bin/env python3

from flask import Flask, render_template
import flask_site.model as model
import random
def create_app(test_config=None):
	"""Create and configure the app.
	
	Parameters
	----------
		test_config - Defaults to None, but can be used to set
					  up config for testing.
	Returns
	-------
		Returns the app.
	"""

	app = Flask(__name__, instance_relative_config=True)
	
	app.config.from_mapping(
		SECRET_KEY='dev'
		)
	if test_config is None:
		# Load the instance config, if it exists, when not testing.
		app.config.from_pyfile('config.py', silent=True)
	else:
		#Load the test config if passed in.
		app.config.from_mapping(test_config)

	@app.route('/')
	def index():
		return 'Index Page'

	@app.route('/hello')
	def hello():
		return 'Hello, World'

	@app.route('/webdev')
	def webdev():
		mod = model.Model()
		real = mod.get_tweet()
		fake = mod.get_fake()
		real_or_fake = [real, fake]
		guess = random.randint(0, 1)
		guess_one = real_or_fake[guess]
		guess_two = real_or_fake[1 - guess]
		return render_template('index.html', real=guess_one, fake=guess_two)


	return app





