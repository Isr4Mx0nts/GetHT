import time
import requests
import tweepy
import os
import re
import sys
import json
import thread
import threading
from lib.correo.clientcorreo import ClientCorreo
from lib.config.appconfig import CorreoConfig
from tweepy.auth import OAuthHandler



class StdOutListener(tweepy.StreamListener ):

	def __init__(self, correo_config, StdOutListener, access_token, access_secret, consumer_key, consumer_secret, path):
		self.access_token = access_token
		self.access_secret = access_secret
		self.consumer_key = consumer_key
		self.consumer_secret = consumer_secret
		self.path = path
		self.StdOutListener = StdOutListener
		self.correo_config = correo_config
	
	def validateConnectionOption(self):
		LIST = self.readFile()
		self.connectTo(LIST)		
		 
		
				
	def connectTo(self, LIST):
		l = StdOutListener(self.correo_config, self.StdOutListener, self.access_token, self.access_secret, self.consumer_key, self.consumer_secret, self.path)
		auth = tweepy.OAuthHandler(self.consumer_key, self.consumer_secret)
		auth.set_access_token(self.access_token, self.access_secret)

<<<<<<< HEAD
=======
		#api = tweepy.API(auth)
		
		#print ("Showing all new tweets for #programming:")
		#stream = tweepy.Stream(auth, l)
		"""
		LIST = self.readFile() 
		List = []
		if (stream != None and auth != None):
			List.append(stream)
			List.append(auth)
			List.append(l)
			return (List)
		else:
			print("Error de autenticacion, verifique credenciales")
			exit(-1)
		"""
		#l = StdOutListener(self.correo_config, self.StdOutListener, self.access_token, self.access_secret, self.consumer_key, self.consumer_secret, self.path)
		#print "Showing all new tweets for #programming:"
>>>>>>> a11710452999ac5718563b4e7e7940f6d6087d0a
		stream = tweepy.Stream(auth, l)
		stream.filter(track=LIST[1],async=True)


	def readFile(self):
		ListH = []
		ListU = []
		LIST = []
		
		if os.path.isfile(self.path+"users"):
			with open(self.path+"users") as my_file:
				for line in my_file:
					ListU.append(line.rstrip('\n'))
		else:
			print("Archivo vacio")
			

		if os.path.isfile(self.path+"hashtags"):
			with open(self.path+"hashtags") as my_file:
				for line in my_file:
					ListH.append(line.rstrip('\n'))
		else:
			print("Empty File")
			
		LIST.append(ListU)
		LIST.append(ListH)
		return LIST


	def detectaAlertaHilo(self, tweet, user, url):#paramas d, u, url
		LIST = self.readFile()#ListC	ListH
		
		config_file_path = os.path.join(os.getcwd(), 'config.yml')
		self.correo_config = CorreoConfig(config_file_path)

<<<<<<< HEAD
		correo_client = ClientCorreo(self.correo_config.get_property('user'), self.correo_config.get_property('pwd'), self.correo_config.get_property('dest'), self.correo_config.get_property('subject'))
		
		session = requests.Session() 

		#matches = re.findall(r'#\w*', line)
		#goo.gl/gZUiCA  #sre  #defacement
		for i in LIST[1]:#Lista de ataques (hashtags)
			matches = re.findall(r'#\w*', tweet)
			if (i in matches):
				print("Esta el hastag en los matches") 
			#matches = re.findall(r'#\w*', tweet)
			#print (matches)
			#if (matches):
=======
	def detectaAlertaHilo(self, tweet, user, url):#paramas d, u, url
		LIST = self.readFile()#ListC	ListH
		
		
		session = requests.Session() 
		for i in LIST[1]:
			if (i in tweet): 
>>>>>>> a11710452999ac5718563b4e7e7940f6d6087d0a
				if (url):
					for j in url:
						if (j['url']):
							urlCortada = j['url']
							resp = session.head(urlCortada, allow_redirects=True)
<<<<<<< HEAD
							for k in LIST[0]:#Lista de clientes
								
								url_redirect = str(resp.url)
								if (k in url_redirect):
									print ("ALERTA con URL")
									correo_client.EnviaCorreo(tweet, user, url_redirect)
									exit(0)
									
								else:
									continue
				else:
					for h in LIST[0]:
						twt = tweet.split(" ")		
						if (h in twt or ("#"+h) in twt):
							print("ALERTA sin URL")
							correo_client.EnviaCorreo(tweet, user, url)
							exit(0)
				
			else:
				continue

		print("Sin alerta")

=======
							for k in LIST[0]:
								url_redirect = str(resp.url)
								if (k in url_redirect):
									print ("ALERTA")
							

							
			

		#print (tweet)
		#print (url)
		clienteCorreo = ClientCorreo(self.correo_config)
		clienteCorreo.funcion()
		
		
		
		#print (LIST)#ListU, ListH

		print("Dentro del hilo--------------------------------------------------",'\n')

>>>>>>> a11710452999ac5718563b4e7e7940f6d6087d0a
		
	def on_data(self, data):
		#print '@%s: %s' % (decoded['user']['screen_name'], decoded['text'].encode('ascii', 'ignore'))
		
		decoded = json.loads(data)
		u = decoded["user"]["screen_name"]
		d = decoded['text']
		n = len(decoded['entities']['urls'])
 		#if (n > 0):
		url = decoded['entities']['urls']
		try:

			t = threading.Thread(target=self.detectaAlertaHilo, args=(d,u,url))
			#thread.start_new_thread( detectaAlertaHilo, (d, u, ))
			t.start()
		except e:
			print "Error: unable to start thread"
			print (e)

		return True

	def on_error(self, status):
		print ("Error")
        	print (status)
