import tweepy
import os
class TwitterClient:
	def __init__(self, access_token, access_secret, consumer_key, consumer_secret, path):
		self.access_token = access_token
		self.access_secret = access_secret
		self.consumer_key = consumer_key
		self.consumer_secret = consumer_secret
		self.path = path
	
	def validateConnectionOption(self, option):
		API = self.connectTo()		
		data = self.readFile(option) #data es lista de users o hashtags
		if (option == "users"):
			self.processUsers(data, API)
		else:
			self.processHashtags(data)

	def processUsers(self, data, API):
		for user in data:
			print (user)
			usr = API.get_user(user)#El ubjeto usuario es el que guarda la informacion
			for friend in usr.friends():
				print friend.screen_name #a quien sigue el usuario

#	def processHashtags(self, data, API):
			

	def connectTo(self):
		
		auth = tweepy.OAuthHandler(self.consumer_key, self.consumer_secret)
		auth.set_access_token(self.access_token, self.access_secret)
		api = tweepy.API(auth)
		if (api != None):
			return api
		else:
			print("Error de autenticacion, verifique credenciales")
			exit(0)

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

if __name__ == "__main__":
	tw = TwitterClient('a', 'b',  'c',  'd',  'e')
	tw.readFiles();
	print ("hola")
