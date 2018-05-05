import urllib2
import searchStudio
from bs4 import BeautifulSoup


anime = "https://myanimelist.net/anime/136/Hunter_x_Hunter"
page = urllib2.urlopen(anime)
soup = BeautifulSoup(page,"html.parser")

##print soup.prettify() to test correctly call page code



##title anime
title = soup.title.string
print title 

##episodes
episode = soup.find('span', id="curEps").string
print ("Episodios: " + episode) 

##rating
ratingValue = soup.find('span', itemprop="ratingValue").string
print ("Classificacao: " + ratingValue) 

##number of members rating
ratingCount = soup.find('span', itemprop="ratingCount").string
print ("Numero de classificadores: " + ratingCount) 

##Studio
studio = ""
print ("Estudio: " + searchStudio.studioSearch(studio,soup))
