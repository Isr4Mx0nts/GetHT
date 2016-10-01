import time
import tweepy
import os
import json
import thread
import threading
import smtplib



class ClientCorreo:
	def __init__(self, correo_config):# user, pwd, dest, subject, body):
		#self.user = user
		#self.pwd = dest
		#self.subject = subject
		#self.body = body
		self.correo_config = correo_config
	def funcion(self):
		print (self.correo_config)
		#twitter_config.get_property('access_token'), twitter_config.get_property('access_secret'), twitter_config.get_property('consumer_key'), twitter_config.get_property('consumer_secret'), twitter_config.get_property('path')
		print ("Dentro de correo")
