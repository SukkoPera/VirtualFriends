#!/usr/bin/env python

import subprocess
import HTMLParser
import re
import os
import datetime
import random

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, RegexHandler
import logging

# Enable logging
logging.basicConfig (format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level = logging.INFO)

logger = logging.getLogger(__name__)


class TeleGiustino:
	_TOKEN = "<fill_me>"

	_REPLACEMENTS = {
		"sukkopera|gurte*": "@sukkopera",
		#~ "steve": "@stevez1974",
		#~ "mak": "@falconmak",
		#~ "angelo": "@angelocavallo1",
		#~ "valeria": "@ieia80",
		#~ "ernesto": "@itpute",
		#~ "linda": "@psiche_erme",
		#~ "marta": "@solo_viola",
		#~ "johnny": "@johnnydavide",
		#~ "cinzia": "@misscinzy",
		#~ "realgiustino": "@realgiustino"
	}

	_SPECIFIC_REPLY_MAP = {
		"ricco|soldi": "RISPOSTATWITTERRICCO",
		"tasse": "RISPOSTATWITTERTASSE",
		"tiaf|fiat|auto|macchina": "RISPOSTATWITTERFIAT",
		"muscolo|muscoli|palestra": "RISPOSTATWITTERNARCISISMO",
		"petto": "RISPOSTATWITTERPETTO",
		"polonia|polacco": "RISPOSTATWITTERPOLACCO",
		"allergia|allergico": "RISPOSTATWITTERALLERGIA",
		"musica": "RISPOSTATWITTERMUSICA",
		"causa|avvocato": "RISPOSTATWITTERCAUSA",
		"cibo|fame|mangia[a-zA-Z]*": "RISPOSTATWITTERCIBO",
		"skate|skateboard|gimmick": "RISPOSTATWITTERSKATE",
		"kickboxing|pugno|pugni|calcio|calci|botte|chuck": "RISPOSTATWITTERKICKBOXING"
	}

	_SCUSA_PATTERN = "scusa"

	_FOTO_PATTERN = "foto.*giustino"

	_FOTO_PATH = "pics"

	def __init__ (self):
		random.seed ()

		thisScript = os.path.realpath (__file__)
		self._mypath = os.path.dirname (thisScript)		# .grm file will be in same dir as executable

		self._updater = Updater (TeleGiustino._TOKEN)

		# Get the dispatcher to register handlers
		dp = self._updater.dispatcher

		# on different commands - answer in Telegram
		dp.add_handler (CommandHandler ("start", self._onStart))
		dp.add_handler (CommandHandler ("help", help))
		dp.add_handler (MessageHandler (Filters.photo, self._onNewPic))
		dp.add_handler (MessageHandler (Filters.text, self._onMessage))

		# log all errors
		dp.add_error_handler (self._onError)

	def start (self):
		# Start the Bot
		self._updater.start_polling ()

		# Run the bot until the you presses Ctrl-C or the process receives SIGINT,
		# SIGTERM or SIGABRT. This should be used most of the time, since
		# start_polling() is non-blocking and will stop the bot gracefully.
		self._updater.idle ()

	def _onStart (self, bot, update):
		bot.sendMessage (update.message.chat_id, text = 'Hi!')

	def _help (self, bot, update):
		bot.sendMessage (update.message.chat_id, text = 'Help!')

	def _onMessage (self, bot, update):
		#~ print str (bot)
		#~ print "chat = " + str (update.effective_chat)
		#~ print "user = " + str (update.effective_user)
		#~ print "msg = " + str (update.effective_message)

		if update.message is not None:
			typ = update.effective_chat.type
			if typ == "private":
				self._onPrivateMessage (bot, update)
			elif typ == "group":
				self._onGroupMessage (bot, update)
			else:
				logger.error ("Unsupported update type: %s" % typ)
		else:
			logger.error ("Update is None")

	def _onPrivateMessage (self, bot, update):
		assert update.message is not None

		msg = update.message.text
		user = update.message.from_user.username
		#~ print update.message.chat_id
		#~ print update.message.from_user.username + ":",
		#~ print update.message.text
		#~ update.message.first_name last_name
		now = datetime.datetime.now ().strftime ("%c")
		logger.info ("[%s] %s: %s" % (now, user, msg))

		# Check if we have a specific reply first
		perla = None
		for pat, startingSymbol in self._SPECIFIC_REPLY_MAP.iteritems ():
			pat = r"\b%s\b" % pat                   # Only match whole words
			rx = re.search (pat, msg, flags = re.IGNORECASE)
			if rx is not None:
				perla = self._getPerla (startingSymbol)
				break

		if perla is None:
			# No specific reply
			perla = self._getPerla ("RISPOSTAMENZIONETWITTER")

		logger.info ("--> %s" % perla)
		update.message.reply_text (text = perla)

	def _onGroupMessage (self, bot, update):
		assert update.message is not None

		msg = update.message.text
		user = update.message.from_user.username

		# Check if we must produce a scusa
		rx = re.search (self._SCUSA_PATTERN, msg, flags = re.IGNORECASE)
		if rx is not None:
			perla = self._getScusa ()
		else:
			rx = re.search (self._FOTO_PATTERN, msg, flags = re.IGNORECASE)
			if rx is not None:
				pic = self._getPic ()
				#bot.send_photo (chat_id = update.message.chat_id, photo = open(pic, 'rb'))
				update.message.reply_photo (photo = open (pic, 'rb'))
				perla = None
			else:
				# Check if we have a specific reply
				perla = None
				for pat, startingSymbol in self._SPECIFIC_REPLY_MAP.iteritems ():
					pat = r"\b%s\b" % pat                   # Only match whole words
					rx = re.search (pat, msg, flags = re.IGNORECASE)
					if rx is not None:
						perla = self._getPerla (startingSymbol)
						break

				if perla is None and bot.username in msg:
					# We were mentioned, so let's give a generic reply
					perla = self._getPerla ("RISPOSTAMENZIONETWITTER")

		if perla is not None:
			now = datetime.datetime.now ().strftime ("%c")
			logger.info ("[%s] %s: %s" % (now, user, msg))
			logger.info ("--> %s" % perla)
			update.message.reply_text (text = perla)

	def _onError (self, bot, update, error):
		logger.warn ('Update "%s" caused error "%s"' % (update, error))

	def _onNewPic (self, bot, update):
		user = update.message.from_user
		photo_file = bot.get_file (update.message.photo[-1].file_id)
		now = datetime.datetime.now ()
		fn = "%s-%s.jpg" % (user["username"], now.strftime ("%Y%m%d%H%M%S"))
		newpicfn = os.path.join (self._FOTO_PATH, fn)
		print "Saving pic to %s" % newpicfn
		photo_file.download (newpicfn)
		#logger.info("Photo of %s: %s" % (user.first_name, 'user_photo.jpg'))
		update.message.reply_text ("Foto ricevuta, grazie!")

	def _getPerla (self, startingSymbol = None):
		try:
			cmd = ["/usr/local/bin/polygen", os.path.join (self._mypath, "virtualgiustino.grm")]
			#cmd = ["polygen", "/home/giorgio/git/vg/virtualgiustino.grm"]
			if startingSymbol is not None:
				cmd.insert (1, "-S")
				cmd.insert (2, startingSymbol)
			perla = subprocess.check_output (cmd).strip ()

			# Do replacements
			for pat, rep in self._REPLACEMENTS.iteritems ():
				pat = r"\b%s\b" % pat			# Only match whole words
				perla = re.sub (pat, rep, perla, flags = re.IGNORECASE)

			# Replace HTML entities
			parser = HTMLParser.HTMLParser ()
			perla = parser.unescape (perla)
		except subprocess.CalledProcessError as ex:
			self.logger.error ("Cannot run Polygen: %s" % str (ex))
			perla = "Sto sbarellando!"
		return perla

	def _getScusa (self):
		try:
			cmd = ["/usr/local/bin/polygen", os.path.join (self._mypath, "virtualjohnny.grm")]
			scusa = subprocess.check_output (cmd).strip ()

			# Replace HTML entities
			parser = HTMLParser.HTMLParser ()
			scusa = parser.unescape (scusa)
		except subprocess.CalledProcessError as ex:
			self.logger.error ("Cannot run Polygen: %s" % str (ex))
			scusa = "Sto sbarellando!"
		return scusa

	def _getPic (self):
		path = os.path.join (self._mypath, self._FOTO_PATH)
		pics = os.listdir (path)
		print "allpics = %s" % str (pics)
		pic = random.choice (pics)
		fullpic = os.path.join (path, pic)
		print "fullpic = %s" % fullpic
		return fullpic

if __name__ == '__main__':
    tg = TeleGiustino ()
    tg.start ()
