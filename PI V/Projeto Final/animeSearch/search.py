import urllib.request
import string
import searchStudio
from textwrap import dedent
from bs4 import BeautifulSoup

replace = "-"

url = "https://myanimelist.net/anime/"

file = open("test.txt", "w", encoding="utf-8")

for x in range(11750, 11759) :

    try:
        page = urllib.request.urlopen(url + str(x))
    except urllib.error.HTTPError as err:
            print("/////////////////////////////////////////////////////////////////////////////")
            print("No anime with the ID " + str(x))

    else:
        soup = BeautifulSoup(page,"html.parser")
        spanTagDark = soup.find_all("span", {"class": "dark_text"})
        
##title anime
        print("/////////////////////////////////////////////////////////////////////////////")
        title = soup.title.string
        title = title.replace(" - MyAnimeList.net\n", "")
        title = title.replace(" ", replace)
        print(title)

        idstr = "Anime ID: " + str(x)
        idstr = idstr.replace("\n", "")
        print(idstr)

##episodes
        episode = soup.find('span', id="curEps").string
        print ("Episodios: " + episode) 

##Score
        ratingValue = soup.find('span', itemprop="ratingValue").string
        print ("Pontuacao/Nota: " + ratingValue) 

##number of members rating
        ratingCount = soup.find('span', itemprop="ratingCount").string
        ratingCount = ratingCount.replace(",", "")
        print ("Numero de votos: " + ratingCount)

##Studio
        studio = searchStudio.studioSearch((""),soup)
        studio = studio.replace(" ", replace)
        print ("Estudio: " + studio)

##rating
        
        for tag in spanTagDark: #search for rating in span = dark_text
            if 'Rating:' in tag:
                rating = tag.parent

#Source

        for tag in spanTagDark:
            if 'Source:' in tag:
                source = tag.parent

        source = str(source)
        sourceLine = source.split("\n")
        source = sourceLine[2]
        source = dedent(source)
        source = source.replace(" ", replace)
        print("Origem: " + source)

#Genres

        for tag in spanTagDark:
            if 'Genres:' in tag:
                genres = tag.parent

        #print(genres)

        genres = str(genres)
        firstIndex = genres.find("")

        firstGenre = secondGenre = thirdGenre = ""
        
        split = genres.split("title=\"")

        if len(split) >= 1:
            firstEnd = split[1].find("\"")
            firstGenre = split[1][:firstEnd]

        if len(split) >= 2: 
            secondEnd = split[2].find("\"")
            secondGenre = split[2][:secondEnd]

        if len(split) >= 3: 
            thirdEnd = split[3].find("\"")
            thirdGenre = split[3][:thirdEnd]

        print("Generos: " + firstGenre + ", " + secondGenre + ", " + thirdGenre)
        

#exclude code(div and scan), normalize rating in string(less indent)
        rating = str(rating)
        ratingLine = rating.split("\n")
        rating = ratingLine[2]
        rating = dedent(rating)
        rating = rating.replace(" ", replace)
        print("Classificacao: " + rating)
        file.write(title + ", " + studio + ", " + rating + ", " + episode + ", " + ratingCount + ", " + ratingValue)

file.close()

