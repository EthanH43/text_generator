#!/usr/bin/env python3

from flask import Flask, render_template
# import flask_site.model as model
import random
import pickle

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

	def get_random(lst):
		"""Returns a random element of the list."""
		
		length = len(lst)
		index = random.randint(0, length-1)
		return lst[index]

	@app.route('/')
	def landing():
		return render_template('landing_index.html')

	@app.route('/hello')
	def hello():
		return 'Hello, World'
	@app.route('/testing')
	def testing():
		# mod = model.Model()
		# path= url_for('data', variable='model.data')
		path = "/Users/Eis4Elephant/Documents/text_generator/website/flask_site/data/model.data"
		with open(path, "rb") as file:
			data = pickle.load(file)

		# real = mod.get_tweet()
		# fake = mod.get_fake()
		real = get_random(data["original_tweets"])
		fake = get_random(data["fake_tweets"])

		real_or_fake = [real, fake]
		guess = get_random([0, 1])
		guess_one = real_or_fake[guess]
		guess_two = real_or_fake[1 - guess]
		return render_template('testing2.html', real=guess_one, fake=guess_two, guess=guess)
	@app.route('/background_process_test')
	def background_process_test():
		print ("Hello")
		return "nothing"
	@app.route('/webdev')
	def webdev():
		# mod = model.Model()
		# path= url_for('data', variable='model.data')
		path = "/Users/Eis4Elephant/Documents/text_generator/website/flask_site/data/model.data"
		with open(path, "rb") as file:
			data = pickle.load(file)

		# real = mod.get_tweet()
		# fake = mod.get_fake()
		real = get_random(data["original_tweets"])
		fake = get_random(data["fake_tweets"])

		real_or_fake = [real, fake]
		guess = get_random([0, 1])
		guess_one = real_or_fake[guess]
		guess_two = real_or_fake[1 - guess]
		return render_template('index.html', real=guess_one, fake=guess_two, guess=guess)


	return app





