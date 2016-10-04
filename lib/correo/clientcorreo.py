import time
import tweepy
import os
import json
import thread
import threading
import smtplib

class ClientCorreo:
	def __init__(self, user, pwd, dest, subject):
		self.user = user
		self.pwd = pwd
		self.dest = dest
		self.subject = subject
	
		

	def EnviaCorreo(self, tweet, user, url):
	
		
		server_ssl = smtplib.SMTP_SSL("smtp.gmail.com", 465)
		server_ssl.ehlo() 
		server_ssl.login(self.user, self.pwd) 
		URL = ""
		if 'url' in url:
			#if (url[0]):
			URL = url[0].get('url')
		else:
			URL = "URL No especificada"	
		
		#else:
		#	URL = "No especificada"
 		text = "Favor de verificar la siguiente informacion: \nCuenta: "+str(user)+"\nTweet: "+str(tweet)
		
		message = 'Subject: %s\n\n%s' % ("Posible ataque efectuado", text)		
		server_ssl.sendmail("Oficina de Seguridad", self.dest, message)

<<<<<<< HEAD

		#server_ssl.quit()	server_ssl.sendmail(FROM, TO, message)
		server_ssl.close()

		print ('successfully sent the mail')
=======
class ClientCorreo:
	def __init__(self, correo_config):# user, pwd, dest, subject, body):
		#self.user = user
		#self.pwd = dest
		#self.subject = subject
		#self.body = body
		self.correo_config = correo_config
	def funcion(self):

		#twitter_config.get_property('access_token'), twitter_config.get_property('access_secret'), twitter_config.get_property('consumer_key'), twitter_config.get_property('consumer_secret'), twitter_config.get_property('path')
		print ("Dentro de correo")
>>>>>>> a11710452999ac5718563b4e7e7940f6d6087d0a
