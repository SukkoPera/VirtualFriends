#!/usr/bin/env python

import subprocess
#~ import HTMLParser
import re
import random

from articdogtriggers import triggers, channels
from twitterbot import TwitterBot
from tweepytwitterinterface import TweepyTwitterInterface
from debuggingtwitterinterface import DebuggingTwitterInterface


class ADTwitterInterface (TweepyTwitterInterface):
	_consumer_key = "<fill_me>"
	_consumer_secret = "<fill_me>"
	_access_token = "<fill_me>"
	_access_token_secret = "<fill_me>"
	
	def __init__ (self, logger):
		super (ADTwitterInterface, self).__init__ (logger)
		self.setOAuthKeys (self._consumer_key, self._consumer_secret, self._access_token, self._access_token_secret)

class ArticDog (TwitterBot):
	_REPLACEMENTS = {
		"\$channel": random.choice (channels)
	}
	
	def __init__ (self):
		super (ArticDog, self).__init__ ("articd0g-%s.log")
		intf = ADTwitterInterface (self.logger)
		#intf = DebuggingTwitterInterface ()
		self.setTwitterInterface (intf)
		
	def makeTweet (self, maxlen = TwitterBot.MAX_TWEET_LEN, key = None):
		while True:
			if key is None:
				key = random.choice (triggers.keys ())
			msg = random.choice (triggers[key])
			msg = msg.decode ("utf-8")
			
			# Do replacements
			for pat, rep in self._REPLACEMENTS.iteritems ():
				msg = re.sub (pat, rep, msg)
			
			if len (msg) <= maxlen:
				break

		return msg

	def handleMention (self, tweet, author, timestamp):
		# Prepare reply mentioning users
		users = self._getMentionedUsers (tweet, author, True)
		msg = ", ".join (users) + ": "

		# Check if we have a specific reply first
		perla = None
		for key in triggers.iterkeys ():
			key2 = r"\b%s\b" % key                   # Only match whole words
			rx = re.search (key2, tweet, flags = re.IGNORECASE)
			if rx is not None:
				perla = self.makeTweet (self.MAX_TWEET_LEN - len (msg), key)
				break

		if perla is None:
			# No specific reply 
			perla = self.makeTweet (self.MAX_TWEET_LEN - len (msg))

		msg += perla
		return msg


if __name__ == "__main__":
	import sys
	from optparse import OptionParser
	
	parser = OptionParser (usage = "usage: %prog [options]", description = "Implements the ArticDog Twitter Bot", version = "%s" % ArticDog.VERSION)
	parser.add_option ("-c", "--check", action = "store_true", help = "Check for mentions and reply to them", default = False)
	parser.add_option ("-t", "--tweet", action = "store_true", help = "Tweet a new message", default = False)
	(options, args) = parser.parse_args ()
	inputFiles = args

	if options.check or options.tweet:
		articdog = ArticDog ()
		
		if options.check:
			articdog.checkForMentions ()
			
		if options.tweet:
			articdog.randomTweet ()
		
		ret = 0
	else:
		parser.print_help ()
		ret = 1

	sys.exit (ret)
