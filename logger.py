#!/usr/bin/env python

import codecs
import os
import sys
import datetime

class Logger (object):
	def __init__ (self, logdir, logfile = None, toStdout = False, debug = False):
		self.logdir = logdir
		self._toStdout = toStdout
		self._debugEnabled = debug
		
		if logfile is None:
			logfile = "%s.log"
		if "%s" in logfile:
			today = datetime.date.today ()
			logfile = logfile % today.strftime ("%Y%m%d")
		fLog_name = os.path.join (self.logdir, logfile);
		self.fLog = codecs.open (fLog_name, "a", encoding = "UTF-8")
		if not self.fLog:
			print >> sys.stderr, "Cannot open log file %s" % fLog_name
			self.fLog = None
		
	def log (self, what, flush = True):
		if self.fLog is not None:
			dt = datetime.datetime.now ()
			ts = dt.strftime ("%d/%m/%Y %H:%M:%S")
			self.fLog.write ("[%s] %s\n" % (ts, what))
			if flush:
				self.fLog.flush ()
			if self._toStdout:
				print what
		else:
			print >> sys.stderr, "Cannot write to log file: %s" % what

	def debug (self, what):
		if self._debugEnabled:
			self.log ("[DEBUG] %s" % what)

	def warning (self, what):
		self.log ("[WARNING] %s" % what)

	def error (self, what):
		self.log ("[ERROR] %s" % what)
