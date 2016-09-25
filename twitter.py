
from twitter import Twitter, OAuth, TwitterHTTPError, TwitterStream
#from twitter import OAuth
#from twitter import TwitterHTTPError
#from twitter import TwitterStream

import json

ACCESS_TOKEN = '778416628090351616-RSgW3Gi4FvlgxdI0L0LToTalRtXV450'
ACCESS_SECRET = 'NbzmypwIj5CoImRIwGs8NQiu2Yl6wTtzp7fkicURPLfi7'
CONSUMER_KEY = 'eoUh6hm3Nvk4M0DCVjq0HJ2AU'
CONSUMER_SECRET = 'PrjgcsbR6N1hwPxzkhh4bzC5vXJunoqGz6CDrlXHtoKG8DaZQm'

oauth = OAuth(ACCESS_TOKEN, ACCESS_SECRET, CONSUMER_KEY, CONSUMER_SECRET)

twitter = Twitter(auth=oauth)

l = twitter.search.tweets(q='#laAdultezEsComplicada', count=5)
print l

for key in (l['statuses']):
	print key['text']
	for i in key['entities']['hashtags']:
		print i
	for j in key['entities']['user_mentions']:
		print j
