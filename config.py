from typing import (List, TypedDict)

class Competition(TypedDict):
	sport       : str
	competition : str

class Game(TypedDict):
	team1 : str
	team2 : str
	odds  : List[float]

T_get_games = List[Game]


discord_url = "https://discord.com/api/webhooks/802102412956532757/BhR57NBLLOylOyCUm0H3M2al57ILuta_c45yJqhOxa-P32b6GGOhUTN1V1KbqfDq205C"

competitions : List[Competition] = [
	{'sport': "football",   'competition': "ligue1"},
	{'sport': "football",   'competition': "liga"},
	{'sport': "football",   'competition': "bundesliga"},
	{'sport': "football",   'competition': "premier-league"},
	{'sport': "football",   'competition': "serie-a"},
	{'sport': "football",   'competition': "primeira"},
	{'sport': "football",   'competition': "serie-a-brasil"},
	{'sport': "football",   'competition': "a-league"},
	{'sport': "football",   'competition': "bundesliga-austria"},
	{'sport': "football",   'competition': "division-1a"},
	{'sport': "football",   'competition': "super-lig"},
	{'sport': "basketball", "competition": "nba"},
	{'sport': "basketball", "competition": "euroleague"},
]
