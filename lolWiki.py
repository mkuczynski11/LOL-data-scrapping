import requests
from bs4 import BeautifulSoup
from handlers import *

url_lec = "https://lol.gamepedia.com/LEC/2021_Season/Spring_Season"
url_lcs = "https://lol.gamepedia.com/LEC/2021_Season/Spring_Season"
url_lck = "https://lol.gamepedia.com/LCK/2021_Season/Spring_Season"
url_lpl = "https://lol.gamepedia.com/LPL/2021_Season/Spring_Season"

teams_lec = findTeams(url_lec)
teams_lcs = findTeams(url_lcs)
teams_lck = findTeams(url_lck)
teams_lpl = findTeams(url_lpl)

scores_lec = findScores(url_lec, teams_lec)
scores_lcs = findScores(url_lcs, teams_lcs)
scores_lck = findScores(url_lck, teams_lck)
scores_lpl = findScores(url_lpl, teams_lpl)

print(scores_lpl)