import urllib2
import searchStudio
from textwrap import dedent
from bs4 import BeautifulSoup


anime = "https://myanimelist.net/anime/1000"
page = urllib2.urlopen(anime)
soup = BeautifulSoup(page,"html.parser")
spanTagDark = soup.find_all("span", {"class": "dark_text"})

#print soup.prettify() #to test correctly call page code



##title anime
title = soup.title.string
print title 

##episodes
episode = soup.find('span', id="curEps").string
print ("Episodios: " + episode) 

##Score
ratingValue = soup.find('span', itemprop="ratingValue").string
print ("Pontuacao/Nota: " + ratingValue) 

##number of members rating
ratingCount = soup.find('span', itemprop="ratingCount").string
print ("Numero de votos: " + ratingCount) 

##Studio
studio = ""
print ("Estudio: " + searchStudio.studioSearch((studio),soup))

##rating
for tag in spanTagDark: #search for rating in span = dark_text
    if 'Rating:' in tag:
        rating = tag.parent

#exclude code(div and scan), normalize rating in string(less indent)
rating = str(rating)
ratingLine = rating.split("\n")
rating = ratingLine[2]
rating = dedent(rating)

print("Classificacao: " + rating)

