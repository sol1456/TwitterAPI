# coding: utf-8
from Api import Client
import time

client = Client('ConsumerKey', 'AccessToken', 'ConsumerSecret', 'AccesssTokenSecret')

print('Enter screen name')
screenName = raw_input('>> ')

print('Enter follow count')
inputCount = raw_input('>> ')

followerList = client.getFollowerByScreenName(screenName)['ids']

count = 0

for userId in followerList:
	if count == inputCount:
		break

	count+= 1
	client.followByUserId(userId)
	print(count)
	time.sleep(1)