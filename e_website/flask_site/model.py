#!/usr/bin/env python3
import tensorflow as tf
import csv
import random
import pickle
import numpy as np

class Model:
	"""Class that implements the ML model.

	Instantiating the class with a file's path
	creates a Keras model. This model will be 
	used to generate the text for the webpage 
	comparison.

	Parameter
	---------
		model_file -> file path to a .h5 file 
					  containing a saved Keras model.
	"""
	__MODELPATH = '/Users/Eis4Elephant/Documents/text_generator/Saved_models/first_char_model.h5'
	__DATAPATH = '/Users/Eis4Elephant/Documents/text_generator/website/flask_site/data/model.data'
	def __init__(self, model_file=''):
		if model_file:
			self._model = tf.keras.models.load_model(model_file)
		else:
			self._model = tf.keras.models.load_model(self.__MODELPATH)
		with open(self.__DATAPATH, 'rb') as file:
			self._model_data = pickle.load(file)

	def get_tweet(self):
		"""Gets a random tweet from _trump_tweets.
		
		Returns:
			Returns a random element from _trump_tweets
		"""
		index = random.randint(0, len(self._model_data['tweets_lst'])-1)
		return self._model_data['tweets_lst'][index]

	def get_fake(self, length=120):
		"""Gets a fake tweet made by the model.

		Returns:
			Returns a tweet generated by the _model.
		"""

		data = self._model_data
		chars = data['chars']
		maxlen = data['maxlen']
		#maxlen = 30
		char_to_index = data['char_to_index']
		index_to_char = data['index_to_char']
		
		starter = self.check_len(self.get_tweet())
		starter = starter[:30]	
		generated = starter
		for i in range(0, length):
			x_pred = np.zeros((1, maxlen, len(chars)), dtype=np.bool)
			for t, char in enumerate(starter):
				x_pred[0, t, char_to_index[char]] = 1

			pred = self._model.predict(x_pred)[0]
			next_index = self.sample(pred)
			next_char = index_to_char[next_index]
				
			generated += next_char
			starter = starter[1:] + next_char		
		return generated

	def sample(self, preds, temperature=1.0):
		"""helper function to sample an index from a probability array."""
		preds = np.asarray(preds).astype('float64')
		preds = np.log(preds) / temperature
		exp_preds = np.exp(preds)
		preds = exp_preds / np.sum(exp_preds)
		probas = np.random.multinomial(1, preds, 1)
		return np.argmax(probas)
	
	def check_len(self, starter):
		"""Checks that the starter length is greater than 30."""
		while len(starter) <= 30:
			starter = self.get_tweet()
		return starter

def make():
	mod = Model()
	return mod.get_fake()

print(make())




