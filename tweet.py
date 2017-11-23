from Api import Client

client = Client('ConsumerKey', 'AccessToken', 'ConsumerSecret', 'AccesssTokenSecret')

client.tweet('Tweet Content')