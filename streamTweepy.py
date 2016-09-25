import tweepy
 
auth = tweepy.OAuthHandler('eoUh6hm3Nvk4M0DCVjq0HJ2AU', 'PrjgcsbR6N1hwPxzkhh4bzC5vX    JunoqGz6CDrlXHtoKG8DaZQm')
auth.set_access_token('778416628090351616-RSgW3Gi4FvlgxdI0L0LToTalRtXV450', 'Nbzmyp    wIj5CoImRIwGs8NQiu2Yl6wTtzp7fkicURPLfi7')
 
api = tweepy.API(auth)
#especificar usuario @
user = api.get_user('raly_montes')

#STREAM
class MyStreamListener(tweepy.StreamListener):
	def on_status(self, status):
        	print(status.text)

if __name__ == '__main__':
	print ("hola")
