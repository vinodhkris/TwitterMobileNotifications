from twitter import *

class TwitterData:
	def __init__(self):
		token = ''
		token_key = ''
		con_secret_key = ''
		con_secret = ''
		self.twitObject = Twitter(auth=OAuth(token, token_key, con_secret, con_secret_key))

	def getTweets(self,user,count):
		x =	self.twitObject.statuses.user_timeline(screen_name=user,count=count)
		tweets = []
		for i in xrange(len(x)):
			tweet = []
			for word in x[i]['text'].split():
				try:
					tweet.append(str(word))
				except:
					continue
			tweets.append(' '.join(tweet))
		return tweets

	def search(self,searchString):
		return self.twitObject.search.tweets(q=searchString)

	def updateStatus(self,statusUpdate):
		self.twitObject.status.update(status=statusUpdate)
		return True