import tweepy
import json

# Authentication details. To  obtain these visit dev.twitter.com

access_token = '778416628090351616-RSgW3Gi4FvlgxdI0L0LToTalRtXV450'
access_token_secret = 'NbzmypwIj5CoImRIwGs8NQiu2Yl6wTtzp7fkicURPLfi7'
consumer_key = 'eoUh6hm3Nvk4M0DCVjq0HJ2AU'
consumer_secret = 'PrjgcsbR6N1hwPxzkhh4bzC5vXJunoqGz6CDrlXHtoKG8DaZQm'

# This is the listener, resposible for receiving data

class StdOutListener(tweepy.StreamListener):
	def on_data(self, data):
		# Twitter returns data in JSON format - we need to decode it first
		decoded = json.loads(data)
		# Also, we convert UTF-8 to ASCII ignoring all bad characters sent by users

		print '@%s: %s' % (decoded['user']['screen_name'], decoded['text'].encode('ascii', 'ignore'))

		print ''

		return True



    def on_error(self, status):

        print status



if __name__ == '__main__':

    l = StdOutListener()

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)

    auth.set_access_token(access_token, access_token_secret)



    print "Showing all new tweets for #programming:"



    # There are different kinds of streams: public stream, user stream, multi-user streams

    # In this example follow #programming tag

    # For more details refer to https://dev.twitter.com/docs/streaming-apis

    stream = tweepy.Stream(auth, l)

    stream.filter(track=['programming'])
