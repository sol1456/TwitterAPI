# coding: utf-8
from Api import Client

client = Client('ConsumerKey', 'AccessToken', 'ConsumerSecret', 'AccesssTokenSecret')

print(client.tweet('tweet content'))
