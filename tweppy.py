import tweepy
import os

auth = tweepy.OAuthHandler('eoUh6hm3Nvk4M0DCVjq0HJ2AU', 'PrjgcsbR6N1hwPxzkhh4bzC5vXJunoqGz6CDrlXHtoKG8DaZQm')
auth.set_access_token('778416628090351616-RSgW3Gi4FvlgxdI0L0LToTalRtXV450', 'NbzmypwIj5CoImRIwGs8NQiu2Yl6wTtzp7fkicURPLfi7')

api = tweepy.API(auth)
#especificar usuario @
user = api.get_user('raly_montes')
print user.screen_name #nombre de usuario
print user.followers_count #numero de seguidores
for friend in user.friends():
	print friend.screen_name #a quien sigue el usuario

#Permite ver todo el time line de un usuario
statuses = api.user_timeline()
if statuses:
	for status in statuses:
		# process status here
		print(status)

	
