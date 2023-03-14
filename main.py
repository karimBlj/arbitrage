import bookmakers.winamax as winamax
import bookmakers.pmu     as pmu
import bookmakers.betclic as betclic
import bookmakers.zebet   as zebet
import bookmakers.netbet  as netbet
import bookmakers.ps3838  as ps3838
import arb
import sys
import log
import config
import traceback
from typing import Dict


from config import Game
# print(ps3838.get_games({'competition': 'nba', 'sport': 'basketball'}))
# exit(0)
log.init()

bookmaker_classes = [
	winamax,
	pmu,
	betclic,
	zebet,
	netbet,
	# ps3838,
]

progress = 0
print(pmu.get_games(config.competitions[0]))

for competition in config.competitions:
	progress += 1
	bookmakers = {}
	for bookmaker in bookmaker_classes:
		class_name = bookmaker.__name__.split(".")[-1]
		try:
			bookmakers[class_name] = bookmaker.get_games(competition)
			log.log(f"{class_name}: " + str(bookmakers[class_name]))
		except:
			log.log(f"Cannot crawl {class_name}: " + traceback.format_exc())
	for game in bookmakers['pmu']:
		games : Dict[str, Game] = {}
		for bookmaker in bookmakers:
			try:
				g = arb.get_game(game, bookmakers[bookmaker])
				if (g):
					games[bookmaker] = g
			except:
				log.log("Error while retrieving games: {}".format(traceback.format_exc()))
		if (competition["sport"] == "football"):
			arb.arb_football(games)
		# if (competition["sport"] == "basketball"):
		# 	arb.arb_basketball(games)
	print("Progess: {:.2f}%".format(progress / len(config.competitions) * 100))
