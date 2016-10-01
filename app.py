import os
from lib.twitter.clienttwitter import StdOutListener#TwitterClient
from lib.config.appconfig import TwitterConfig
from lib.config.appconfig import CorreoConfig
import sys


#for arg in sys.argv:
#if (len(sys.argv) != 2):
#	print("Uso: python app.py [option]")
#	exit(0)
#option = sys.argv[1]
config_file_path = os.path.join(os.getcwd(), 'config.yml')

twitter_config = TwitterConfig(config_file_path)
correo_config = CorreoConfig(config_file_path)

twitter_client = StdOutListener(correo_config, StdOutListener, twitter_config.get_property('access_token'), twitter_config.get_property('access_secret'), twitter_config.get_property('consumer_key'), twitter_config.get_property('consumer_secret'), twitter_config.get_property('path'))

twitter_client.validateConnectionOption()
