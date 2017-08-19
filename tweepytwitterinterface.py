#!/usr/bin/env python

import datetime
import unicodedata

# pip install tweepy
import tweepy

from twitterbot import TwitterInterface


class TweepyTwitterInterface (TwitterInterface):
	def setOAuthKeys (self, consumer_key, consumer_secret, access_token, access_token_secret):
		"""== OAuth Authentication ==
		This mode of authentication is the new preferred way
		of authenticating with Twitter.

		The consumer keys can be found on your application's Details
		page located at https://dev.twitter.com/apps (under "OAuth settings")

		The access tokens can be found on your applications's Details
		page located at https://dev.twitter.com/apps (located 
		under "Your access token")"""
		auth = tweepy.OAuthHandler (consumer_key, consumer_secret)
		auth.set_access_token (access_token, access_token_secret)
		self._api = tweepy.API (auth)
		self._me = "@" + self._api.me ().screen_name
		self.logger.debug ("Logged in to %s (%s)" % (self._api.me ().name, self._me))
		
	def tweet (self, perla, in_reply_to_status_id = None):
		self.logger.log ("Tweeting: %s%s" % (perla, " (In reply to: %s)" % in_reply_to_status_id if in_reply_to_status_id is not None else ""))
		self._api.update_status (perla, in_reply_to_status_id = in_reply_to_status_id)
		
	def getMentions (self, newerThan = None):
		ret = []
		for mention in self._api.mentions_timeline ():
			#~ print mention, type (mention)
			#~ print dir (mention)
			#~ if type (mention.text) is unicode:
				#~ tweet = unicodedata.normalize ("NFKD", mention.text).encode ("ascii", "ignore")
			#~ else:
			tweet = mention.text
			if newerThan is None or mention.created_at >= newerThan:			# mention.created_at is UTC time!
				author = "@" + mention.user.screen_name
				#~ self.logger.debug ("Mentioned by %s: %s (%s)" % (author, tweet, mention.created_at))
				m = (tweet, author, mention.created_at, mention.id)
				ret.append (m)
		return ret

	def myNick (self):
		return self._me
