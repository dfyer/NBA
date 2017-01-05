from urllib import request
from bs4 import BeautifulSoup as bs


url = 'http://stats.nba.com/game/#!/0021600528/'
with request.urlopen(url) as resp:
    soup = bs(resp, 'html.parser')
    # Game Status: Final?
    print(soup.find_all(attrs={'class': 'game-summary__state'}))
    # Game
