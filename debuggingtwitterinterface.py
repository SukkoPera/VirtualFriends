#!/usr/bin/env python

import datetime

from twitterbot import TwitterInterface


class DebuggingTwitterInterface (TwitterInterface):
	def _debug (self, what):
		print "[%s]: %s" % (self.__class__.__name__, what)
		pass
		
	def tweet (self, perla, in_reply_to_status_id = None):
		self._debug ("Would tweet: %s (In reply to: %s)" % (perla, in_reply_to_status_id))
		
	def getMentions (self, newerThan = None):
		ret = [
			("@VirtualGiustino @SukkoPera sul petto?", "@stevez1974", datetime.datetime (2014, 3, 3, 21, 36, 35), 1),
			("@VirtualGiustino @stevez1974: Hai aggiustato sta cavolo di tastiera???", "@SukkoPera", datetime.datetime (2014, 3, 3, 21, 29, 46), 2),
			("@VirtualGiustino @psiche_erme @AngeloCavallo1 @misscinzy @SukkoPera siete fuori come il petto di Giustino", "@stevez1974", datetime.datetime (2014, 3, 3, 19, 29, 32), 3),
			("@VirtualGiustino ci sono ragazze?", "@stevez1974", datetime.datetime (2014, 3, 3, 22, 00, 00), 3),
			("@VirtualGiustino sei un bot?", "@SukkoPera", datetime.datetime (2014, 3, 3, 22, 00, 00), 3),
			("@VirtualGiustino Ti piacciono i depeche?", "@SukkoPera", datetime.datetime (2014, 3, 3, 22, 00, 00), 3)
		]
		return ret

	def myNick (self):
		return "@VirtualGiustino"
