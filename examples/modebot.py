# -*- coding: utf-8 -*-
# -*- tab-width: 4; use-tabs: 1 -*-
# vim:tabstop=4:noexpandtab:
"""
Changes modes.
"""
from __future__ import division, absolute_import, with_statement
from rconbot.bot import Bot, recallback, command, loadpassfromconfig
from rconbot.nexuiz import Commands
import random
__all__ = 'ModeBot',

# Thank you <http://toolz.nexuizninjaz.com/cvar/index.php?search=g_>
modes = {
	'g_dm':'Deathmatch', 
	'g_tdm':'TEAM Deathmatch', 
	'g_ctf':'Capture the Flag', 
	'g_domination':'Domination', 
#	'g_runematch':'Rune match', 
	'g_lms':'Last Man Standing', 
#	'g_arena':'Arena', # Too problematic with few players
	'g_keyhunt':'Key Hunt',
#	'g_onslaught':'Onslaught', # Breaks the server
# New modes g_assault, g_race
	}

# g_casings, g_classbased, g_throughfloor
# g_bugrigs - Enable Big Rigs physics (aka racing comedy hour)
# g_jetpack - Enable jetpack. 
# g_pinata - on death, all weapons drop (not just current)
# g_turrets - AI turrets to destroy players
# g_weaponarena - given list of weapons, can only use those weapons

mutators = {
	'g_cloaked' : ('cloaking', 0),
	'g_footsteps' : ('no footsteps', 1),
	'g_grappling_hook' : ('off-hand hook', 0),
	'g_laserguided_missile' : ('laser-guided rockets', 0),
	'g_midair' : ('midair-only', 0),
	'g_vampire' : ('vampire', 0),
	'g_minstagib' : ('minstagib', 0),
	'g_nixnex' : ('no items', 0),
	'g_nixnex_with_laser' : ('no items but laser', 0),
#Removed
#	'g_instagib' : ('instagib', 0),
#	'g_rocketarena' : ('rocket arena', 0),
	}

mutator_chance = 1/10

class ModeBot(Bot):
	_newmap = True
	_random = random.SystemRandom()
	@recallback('^.* has turned (?P<name>.*) into slag$', stripcolors=True)
	@recallback('^(?P<name>.*) turned into hot slag$', stripcolors=True)
	def slag(self, text, name):
		# self is from Bot
		self.say("%s will make good bullets. *pour*" % name)
	
	@recallback(r'^\^4(?P<name>.*)\^4 connected$', stripcolors=False)
	def hello(self, text, name):
		self._newmap = True
		print "hello: %r" % text
		self.say("Hello %s" % name)
	
	@recallback(r'^.* connected$', stripcolors=True)
	@recallback(r'^:vote:', stripcolors=True)
	def clearmap(self, text):
		self._newmap = True
	
	@command
	def spam(self, *pargs):
		print "Command test: %r" % (pargs,)
	
	@command
	def newtype(self):
		mode = self._random.choice(modes.keys())
		newmodes = dict((m, int(m==mode)) for m in modes.iterkeys())
		self.setcvars(**newmodes)
		txt = "The next game type will be %s" % modes[mode]
		newmutators = dict((m, v[1]) for m,v in mutators.iteritems())
		if self._random.random() < mutator_chance:
			mut = self._random.choice(mutators.keys())
			newmutators[mut] = int(not newmutators[mut])
			txt += " (with %s)" % mutators[mut][0]
		self.setcvars(**newmutators) # Also reset previously set mutators
		self.say(txt)
	
	@recallback(r'^.* wins.$', stripcolors=True)
	def newtype_cb(self, text):
		if self._newmap:
			self.newtype()
			self._newmap = False

if __name__ == '__main__':
	import os
	from rconbot.bot import loadpassfromconfig
	from rconbot.utils import filesystem

	filesystem.addpath(os.path.join(os.path.dirname(__file__), 'data'))
	filesystem.reload()
	ModeBot.run(loadpassfromconfig('server.cfg'))

