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

	@app.route('/spike')
	def landing():
		return render_template('landing_index.html')

	@app.route('/hello')
	def hello():
		return 'Hello, World'
	@app.route('/')
	def testing():
		path = "/Users/Eis4Elephant/Documents/text_generator/website/flask_site/data/model.data"
		with open(path, "rb") as file:
			data = pickle.load(file)

		real = get_random(data["original_tweets"])
		fake = get_random(data["fake_tweets"])

		real_shake = get_random(data["real_shake"])
		fake_shake = get_random(data["fake_shake"])

		real_or_fake = [real, fake]
		guess = get_random([0, 1])
		guess_one = real_or_fake[guess]
		guess_two = real_or_fake[1 - guess]

		shake_real_or_fake = [real_shake, fake_shake]
		shake_guess_one = shake_real_or_fake[guess]
		shake_guess_two = shake_real_or_fake[1 - guess]

		# if guess is 0 than the 'real' will be real and fake will be fake, if its 1 than opposite
		if guess == 1:
			return render_template('main_2.html', real=guess_one, fake=guess_two, real_shake=shake_guess_one, fake_shake=shake_guess_two) # main_2
		else:
			return render_template('main_1.html',real=guess_one, fake=guess_two, real_shake=shake_guess_one, fake_shake=shake_guess_two)

	@app.route('/haik')
	def webdevhaik():
		path = "/Users/Eis4Elephant/Documents/text_generator/website/flask_site/data/model.data"
		with open(path, "rb") as file:
			data = pickle.load(file)

		real = get_random(data["original_tweets"])
		fake = get_random(data["fake_tweets"])

		real_or_fake = [real, fake]
		guess = get_random([0, 1])
		guess_one = real_or_fake[guess]
		guess_two = real_or_fake[1 - guess]
		# if guess is 0 than the 'real' will be real and fake will be fake, if its 1 than opposite
		if guess == 1:
			return render_template('main_2.html', real=guess_one, fake=guess_two) # main_2
		else:
			return render_template('main_1.html',real=guess_one, fake=guess_two)

	@app.route('/jackson')
	def webdevjackson():
		path = "/Users/schuylerjackson/text_generator/website/flask_site/data/model.data"
		with open(path, "rb") as file:
			data = pickle.load(file)

		real = get_random(data["original_tweets"])
		fake = get_random(data["fake_tweets"])

		real_or_fake = [real, fake]
		guess = get_random([0, 1])
		guess_one = real_or_fake[guess]
		guess_two = real_or_fake[1 - guess]
		# if guess is 0 than the 'real' will be real and fake will be fake, if its 1 than opposite
		if guess == 1:
			return render_template('main_2.html', real=guess_one, fake=guess_two) # main_2
		else:
			return render_template('main_1.html',real=guess_one, fake=guess_two)
		
	@app.route('/background_process_test')
	def background_process_test():
		print ("Hello")
		return "nothing"
	

	return app





