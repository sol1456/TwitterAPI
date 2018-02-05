# coding: utf-8
from Api import Client
import time

client = Client('ConsumerKey', 'AccessToken', 'ConsumerSecret', 'AccesssTokenSecret')

print('Enter screen name')
screenName = raw_input('>> ')

print('Enter remove count')
inputCount = raw_input('>> ')

followerList = client.getFollowerByScreenName(screenName)['ids']

count = 0

for userId in followerList:
	if count == inputCount:
		break

	if userId not in followerList:
		client.removeByUserId(userId)
		count+= 1
		print(count)
		time.sleep(1)