import time
import tweepy
import os
import json
import thread
import threading
from lib.correo.clientcorreo import ClientCorreo
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
		print "Showing all new tweets for #programming:"
		stream = tweepy.Stream(auth, l)
		stream.filter(track=['programming'],async=True)


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
				
	#def processUsers(self, dataU, dataH, lista):	
	#	stream = tweepy.Stream(lista[0], lista[1])
	#	stream.filter(track=['programming'])



	def detectaAlertaHilo(self, tweet, user):#paramas d, u
		LIST = self.readFile() 
		clienteCorreo = ClientCorreo(self.correo_config)
		clienteCorreo.funcion()


		print("Dentro del hilo--------------------------------------------------",'\n')
		print(tweet)
		print (user)
		
	def on_data(self, data):
		#print '@%s: %s' % (decoded['user']['screen_name'], decoded['text'].encode('ascii', 'ignore'))
		
		decoded = json.loads(data)
		u = decoded["user"]["screen_name"]
		d = decoded['text']
		print (decoded['user']['screen_name'])
		print (decoded['text'])
		n = len(decoded['entities']['urls'])
		print decoded['entities']['urls']
 		if (n > 0):
			for i in decoded['entities']['urls']:
				print i
		print ("N es: ", n)
		#url = decoded['entities']['urls'][0]
		#print (url)
	
		try:

			t = threading.Thread(target=self.detectaAlertaHilo, args=(d,u))
			#thread.start_new_thread( detectaAlertaHilo, (d, u, ))
			t.start()
		except:
			print "Error: unable to start thread"

		return True

	def on_error(self, status):
		print ("ERRRRRROOOOOOOOOOOOORRRRRRRRRRR")
        	print status


