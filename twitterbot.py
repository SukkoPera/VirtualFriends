#!/usr/bin/env python

import os
import re
import tempfile
import datetime
import unicodedata

import logger


class TwitterInterface (object):
	def __init__ (self, logger):
		# Don't do anything peculiar here, since this dummy interface is always initialized by TwitterBot instances
		self.logger = logger
	
	def tweet (self, perla, in_reply_to_status_id = None):
		self.logger.log ("Would tweet: %s (In reply to: %s)" % (perla, in_reply_to_status_id))
		
	def getMentions (self, newerThan = None):
		return []
		
	def myNick (self):
		return "@BaseTwitterInterface"

		
class TwitterBot (object):
	VERSION = "0.3 (02/04/2014)"
	MAX_TWEET_LEN = 140
	_TMP_DIR = tempfile.gettempdir ()		# Lastrun files will be created here
	_LOG_DIR = "log"
	_LASTRUN_FMT = "%Y-%m-%d %H:%M:%S"
	
	def __init__ (self, logfile = None):
		self.logger = logger.Logger (logdir = self._LOG_DIR, logfile = logfile) #, debug = True)
		self._twitterInterface = TwitterInterface (self.logger)		# Init the dummy interface, can always setTwitterInterface() if a different one is needed

	def setTwitterInterface (self, twitterInterface):
		self._twitterInterface = twitterInterface

	def _getLastRunFilename (self):
		filteredNick = re.sub (r"[^A-Za-z0-9]", "", self._twitterInterface.myNick ()).lower ()
		assert len (filteredNick) > 0
		fn = os.path.join (self._TMP_DIR, "%s.lastrun" % filteredNick)
		return fn

	def _readLastRunTime (self):
		self._lastrun = None
		try:
			with open (self._getLastRunFilename (), "r") as fp:
				ts = fp.readline ().strip ()
				self._lastrun  = datetime.datetime.strptime (ts, self._LASTRUN_FMT)
				self.logger.debug ("Last run time: %s" % self._lastrun)
		except ValueError as ex:
			# Invalid time in LASTRUN_FILE, do nothing
			self.logger.warning (str (ex))
			pass
		except IOError as ex:
			# Missing LASTRUN_FILE, do nothing
			self.logger.warning (str (ex))

	def _writeLastRunTime (self):
		with open (self._getLastRunFilename (), "w") as fp:
			fp.write (datetime.datetime.utcnow ().strftime (self._LASTRUN_FMT))
			fp.write ("\n# Above time is UTC\n")

	def _getMentionedUsers (self, tweet, author, includeAuthor = True):
		# Get other mentioned users
		rx = re.compile (r"(@\w+)")
		users = rx.findall (tweet)
		#~ self._debug ("Mentioned users: %s" % users)
		if author.lower () not in (u.lower () for u in users):
			users.insert (0, author)
			#~ self._debug ("Added author to users: %s" % users)

		# Remove ourselves if present
		try:
			# Mess to remove a string from a list case-insensitively
			x = [u.lower () for u in users].index (self._twitterInterface.myNick ().lower ())
			users.pop (x)
			#~ self._debug ("Removed ourselves from users: %s" % users)
		except ValueError:
			# Not present
			pass
		
		return users
	
		
	############################################################################
	# PUBLIC METHODS
	############################################################################
		
	def checkForMentions (self):
		self._readLastRunTime ()
		if self._lastrun is not None:
			for mention in self._twitterInterface.getMentions (self._lastrun):
				self.logger.debug ("Found mention: '%s' (%s) by '%s' at %s" % (mention[0], mention[3], mention[1], mention[2].strftime ("%c UTC")))
				msg = self.handleMention (*mention[0:3])		# id is not necessary
				if msg is not None:
					self.logger.log ("Replying to tweet '%s' (%s) by '%s' with '%s'" % (mention[0], mention[3], mention[1], msg))
					self._twitterInterface.tweet (msg, in_reply_to_status_id = mention[3])
		self._writeLastRunTime ()
		
	def randomTweet (self):
		tweet = self.makeTweet ()
		self._twitterInterface.tweet (tweet)
		
	
	############################################################################
	# METHODS TO OVERRIDE
	############################################################################
	
	def makeTweet (self):
		raise NotImplementedError
		
	def handleMention (self, text, author, timestamp, tweetId):
		raise NotImplementedError
