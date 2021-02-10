import requests
from bs4 import BeautifulSoup

def findTeams(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.content,'html.parser')

    table = soup.find("table", class_="wikitable2 standings")
    names = table.find_all("a", class_="catlink-teams tWACM tWAFM tWAN to_hasTooltip")

    teams = []
    for n in names:
        teams.append(n.text)
    
    return teams

def findScores(url, teams):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    table = soup.find("table", class_="wikitable2 standings")

    scores = {}
    for t in teams:
        name = table.find("a", string=t)
        scoreSibling = name.parent.parent.parent.parent
        score = scoreSibling.find('td').next_sibling.next_sibling.text
        detector = score.split(" ")
        scores[t] = (int(detector[0]),int(detector[2]))
    return scores