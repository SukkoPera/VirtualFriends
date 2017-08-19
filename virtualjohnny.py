#!/usr/bin/env python

import subprocess
import HTMLParser
import re
import os
import sys

from twitterbot import TwitterBot
from tweepytwitterinterface import TweepyTwitterInterface
from debuggingtwitterinterface import DebuggingTwitterInterface


class VJTwitterInterface (TweepyTwitterInterface):
	_consumer_key = "<fill_me>"
	_consumer_secret = "<fill_me>"
	_access_token = "<fill_me>"
	_access_token_secret = "<fill_me>"
	
	def __init__ (self, logger):
		super (VJTwitterInterface, self).__init__ (logger)
		self.setOAuthKeys (self._consumer_key, self._consumer_secret, self._access_token, self._access_token_secret)

class VirtualJohnny (TwitterBot):
	_REPLACEMENTS = {
#		"\$channel": random.choice (channels)
	}
	
	def __init__ (self):
		super (VirtualJohnny, self).__init__ ("virtualjohnny-%s.log")
		intf = VJTwitterInterface (self.logger)
		#intf = DebuggingTwitterInterface (self.logger)
		self.setTwitterInterface (intf)
		thisScript = os.path.realpath (__file__)
		self._mypath = os.path.dirname (thisScript)		# .grm file will be in same dir as executable
		
	def makeTweet (self, maxlen = TwitterBot.MAX_TWEET_LEN, startingSymbol = None):
		try:
			while True:
				#~ sys.path.insert (0, "/usr/local/bin")
				#~ print "Path: %s" % ":".join (sys.path)
				#cmd = ["/usr/local/bin/polygen", "/home/vgiustino/virtualgiustino.grm"]
				cmd = ["/usr/local/bin/polygen", os.path.join (self._mypath, "virtualjohnny.grm")]
				#cmd = ["polygen", "/home/giorgio/git/vg/virtualgiustino.grm"]
				if startingSymbol is not None:
					cmd.insert (1, "-S")
					cmd.insert (2, startingSymbol)
				perla = subprocess.check_output (cmd).strip ()

				# Do replacements
#				for pat, rep in self._REPLACEMENTS.iteritems ():
#					pat = r"\b%s\b" % pat			# Only match whole words
#					perla = re.sub (pat, rep, perla, flags = re.IGNORECASE)
				
				# Replace HTML entities
				parser = HTMLParser.HTMLParser ()
				perla = parser.unescape (perla)
				
				if len (perla) <= maxlen:
					break
		except subprocess.CalledProcessError as ex:
			self.logger.error ("Cannot run Polygen: %s" % str (ex))
			perla = "Sto sbarellando!"
		return perla

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
	
	parser = OptionParser (usage = "usage: %prog [options]", description = "Implements the Virtual Johnny Twitter Bot", version = "%s" % VirtualJohnny.VERSION)
	parser.add_option ("-c", "--check", action = "store_true", help = "Check for mentions and reply to them", default = False)
	parser.add_option ("-t", "--tweet", action = "store_true", help = "Tweet a new message", default = False)
	(options, args) = parser.parse_args ()
	inputFiles = args

	if options.check or options.tweet:
		vjohnny = VirtualJohnny ()
		
		if options.check:
			vjohnny.checkForMentions ()
			
		if options.tweet:
			vjohnny.randomTweet ()
		
		ret = 0
	else:
		parser.print_help ()
		ret = 1

	sys.exit (ret)
