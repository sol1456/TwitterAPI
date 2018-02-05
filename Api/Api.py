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




      def tweetText(self, text):
        return self.request('POST', PATH.TWEET, {'status': text})



      def getSettings(self):
   	    return self.request('GET', PATH.SETTINGS)

      def updateSettings(self, params):
        return self.request('POST', PATH.SETTINGS, params)



      def getBlockedUserIds(self):
        return self.request('GET', PATH.ID_BLOCKED)

      def getBlockedUserList(self):
        return self.request('GET', PATH.U_BLOCKED)



      def getUserByUserId(self, userId):
        return self.request('GET', PATH.USER, {'user_id': userId})

      def getUserByScreenName(self, screenName):
        return self.request('GET', PATH.USER, {'screen_name': screenName})



      def getFollowerByUserId(self, userId):
        return self.request('GET', PATH.FOLLOWERS, {'user_id': userId})

      def getFollowerByScreenName(self, screenName):
        return self.request('GET', PATH.FOLLOWERS, {'screen_name': screenName})







      def followByUserId(self, userId):
        return self.request('POST', PATH.FOLLOW, {'user_id': userId})

      def followByScreenName(self, screenName):
        return self.request('POST', PATH.FOLLOW, {'screen_name': screenName})



      def removeByUserId(self, userId):
        return self.request('POST', PATH.REMOVE, {'user_id': userId})

      def removeByScreenName(self, screenName):
        return self.request('POST', PATH.REMOVE, {'screen_name': screenName})



      def updateProfile(self, params):
        return self.request('POST', PATH.PROFILE, params)

      def updateProfileImage(self, filePath):
        return self.request('POST', PATH.IMAGE, {'image': open(filePath, 'rb').read()})



      def updateProfileBanner(self, filePath):
        return self.request('POST', PATH.U_BANNER, {'banner': str(open(filePath, 'rb').read())})

      def removeProfileBanner(self):
        return self.request('POST', PATH.R_BANNER)