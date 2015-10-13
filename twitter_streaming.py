#Import the necessary methods from tweepy library
import json
import tweepy
import BasicGUI
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

#Variables that contains the user credentials to access Twitter API 
access_token = '2874054435-t8ARu4lPounEZ75lJGLJygdSRrNdlMtRctySSTZ'
access_token_secret = 'lxl0sw2fRJuZns9RuEpYMnrwe1SiEoILwHtmh7JJioANx'
consumer_key = 'MVps6OFMNCkYfMnA2W7TVCmLs'
consumer_secret = 'Js2qWnSvNbLq0wRiQCP4ZBeRd1lpQr6A5tvS7JvPxHYzvdGXWu'


#This is a basic listener that just prints received tweets to stdout.
class StdOutListener(StreamListener):
	search = 'pony'
	def __init__(self):
		self.information = ""
		self.n = 1
		self.m = 1
	def on_data(self, data):
		if self.n < self.m:
			json_load = json.loads(data)
			texts = json_load['text']
			coded = texts.encode('utf-8')
			s = str(coded)
			print(s)
			self.information = s
			f = open('mydata.txt', 'a')
			f.write(s)
			f.write('\n')
			f.close()
			self.n += 1
			return s
		else:
			return None
		
	def on_error(self, status):
		print(status)
	


#if __name__ == '__main__':
	#This handles Twitter authetification and the connection to Twitter Streaming API
#	l = StdOutListener()
#	auth = OAuthHandler(consumer_key, consumer_secret)
#	auth.set_access_token(access_token, access_token_secret)
#	stream = Stream(auth, l)
	#This line filter Twitter Streams to capture data by the keywords: 'python', 'javascript', 'ruby'
#	stream.filter(track=[l.search])

	