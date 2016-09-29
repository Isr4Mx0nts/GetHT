import tweepy
import os
import json
class TwitterClient:
	def __init__(self, access_token, access_secret, consumer_key, consumer_secret, path):
		self.access_token = access_token
		self.access_secret = access_secret
		self.consumer_key = consumer_key
		self.consumer_secret = consumer_secret
		self.path = path
	
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
		l = StdOutListener()
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
		"""
		for user in dataU:
			usr = API.get_user(user)#El ubjeto usuario es el que guarda la informacion
			#for tweet in tweepy.Cursor(API.search,q=user,rpp=1,result_type="recent",include_entities=True,).    items():
			#       print (tweet.created_at)
			#       print (tweet.text)
			for hashtag in dataH:
				for tweet in tweepy.Cursor(API.search, q=(hashtag)).items(5):
					nombre = str(tweet.author.screen_name)
					if (user == nombre):
						print ("Screen-name:", tweet.author.screen_name.encode('utf8'))
						print ("Tweet:", tweet.text.encode('utf8'))
						print tweet.entities.get('hashtags')
		"""
		#l = StdOutListener()
		#auth = tweepy.OAuthHandler(self.consumer_key, self.consumer_secret)
		#auth.set_access_token(self.access_token, self.access_secret)
		#print "Showing all new tweets for #programming:"
		
		stream = tweepy.Stream(lista[1], lista[2])
		stream.filter(track=['programming'])

	def processHashtags(self, data, stream):
		for i in data:
			search_result = API.search(i)#, rpp=1)
			for j in search_result:
				print ('\n')
				print j.text
		exit(0)



class StdOutListener(tweepy.StreamListener):
	def on_data(self, data):
		#print '@%s: %s' % (decoded['user']['screen_name'], decoded['text'].encode('ascii', 'ignore'))
		#print (decoded)
		decoded = json.loads(data)

		print (decoded['user']['screen_name'])
		print (decoded['text'])

		if ("raly_montes" == decoded['user']['screen_name']):
			print ("ALERTA",'\n')
		return True

	def on_error(self, status):
        	print status
