# coding: utf-8
from .EndPoint import PATH
from requests_oauthlib import OAuth1Session

import json, requests

class Client:

   def __init__(self,
		         ConsumerKey,
		         AccessToken,
		         ConsumerSecret,
		         AccesssTokenSecret
		        ):

      self.client = OAuth1Session(
                 ConsumerKey,
                 ConsumerSecret,
                 AccessToken,
                 AccesssTokenSecret
                 )

   def request(self, method, url, params=None):
   	if method == 'GET':
   		req = self.client.get(url, params=params)
   		return json.loads(req.text)

   	if method == 'POST':
   		return self.client.post(url, params)



   'POST Method'


   def tweet(self, text):
   	return self.request('POST', PATH.TWEET, {'status': text})

   def updateProfile(self, params):
   	return self.request('POST', PATH.PROFILE, params)

   def updateSettings(self, params):
   	return self.request('POST', PATH.SETTINGS)

   def updateProfileImage(self, filePath):
   	file = {'image': open(filePath, 'rb').read()}
   	return self.request('POST', PATH.IMAGE, file)

   def updateProfileBanner(self, filePath):
   	file = {'banner': str(open(filePath, 'rb').read())}
   	return self.request('POST', PATH.U_BANNER, file)

   def removeProfileBanner(self):
   	return self.request('POST', PATH.R_BANNER)
   

   'GET Method'

   def getSettings(self):
   	return self.request('GET', PATH.SETTINGS)

   def getBlockedUserIds(self):
   	return self.request('GET', PATH.G_BLOCK1)

   def getUserByScreenName(self, screen_name):
   	return self.request('GET', PATH.USER, {'screen_name': screen_name})

   