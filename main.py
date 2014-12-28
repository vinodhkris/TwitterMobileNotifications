from TwitterData import TwitterData
from Way2SMS import SMS 

s = SMS()
t = TwitterData()
tweets = t.getTweets("philo_quotes",40)
number = ''
for i in xrange(len(tweets)):
	print i,tweets[i]
	s.send_message(number,tweets[i])
