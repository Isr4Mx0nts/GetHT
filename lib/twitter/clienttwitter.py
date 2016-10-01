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
	
	def validateConnectionOption(self, option):
		lista = self.connectTo(option)		
		dataU = self.readFile("users") #data es lista de users o hashtags
		dataH = self.readFile("hashtags")
		if (option == "users"):
			self.processUsers(dataU, dataH, lista)
		elif(option == "hashtags"):
			self.processHashtas(dataU, dataH, lista)		

				
	def connectTo(self, option):
		
		print (option)		
		auth = tweepy.OAuthHandler(self.consumer_key, self.consumer_secret)
		auth.set_access_token(self.access_token, self.access_secret)
		#api = tweepy.API(auth)
		l = StdOutListener(self.correo_config, self.StdOutListener, self.access_token, self.access_secret, self.consumer_key, self.consumer_secret, self.path)
		print "Showing all new tweets for #programming:"
		stream = tweepy.Stream(auth, l)
		
		List = []
		if (stream != None and auth != None):
			List.append(stream)
			List.append(auth)
			List.append(l)
			return (List)
		else:
			print("Error de autenticacion, verifique credenciales")
			exit(-1)
		
		#l = StdOutListener()
		#print "Showing all new tweets for #programming:"
		#stream = tweepy.Stream(auth, l)
		# ------------------- stream.filter(track=['programming'])

	def readFile(self, option):
		ListOption = []
		if (option == "users"):
			if os.path.isfile(self.path+"users"):
				with open(self.path+"users") as my_file:
					for line in my_file:
						ListOption.append(line.rstrip('\n'))
			if(ListOption):
				return ListOption
			else:
				print("Empty File")
				exit(0)
		elif (option == "hashtags"):
			if os.path.isfile(self.path+"hashtags"):
				with open(self.path+"hashtags") as my_file:
					for line in my_file:
						ListOption.append(line.rstrip('\n'))
				if(ListOption):
					return ListOption
				else:
					print("Empty File")
					exit(0)
	def processUsers(self, dataU, dataH, lista):
		
		
		stream = tweepy.Stream(lista[0], lista[1])
		stream.filter(track=['programming'])

	def processHashtags(self, data, stream):
		for i in data:
			search_result = API.search(i)#, rpp=1)
			for j in search_result:
				print ('\n')
				print j.text
		exit(0)


	def detectaAlertaHilo(self, tweet, user):#paramas d, u
		dataU = self.readFile("users") #data es lista de users o hashtags
		dataH = self.readFile("hashtags")
		clienteCorreo = ClientCorreo(self.correo_config)
		clienteCorreo.funcion()


		print("Dentro del hilo",'\n')
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
			for string in ['entities']['urls']:
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
        	print status



