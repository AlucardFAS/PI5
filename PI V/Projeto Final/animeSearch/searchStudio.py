# searchStudio.py

import urllib2
from bs4 import BeautifulSoup

def studioSearch(studio,soup):

    if(soup.find_all('a', title="Kinema Citrus")):
        studio = "Kinema Citrus"
    elif(soup.find_all('a', title="Bones")):
        studio = "Bones"
    elif(soup.find_all('a', title="A-1 Pictures")):
        studio = "A-1 Pictures"
    elif(soup.find_all('a', title="Production I.G")):
        studio = "Production I.G"
    elif(soup.find_all('a', title="Kyoto Animation")):
        studio = "Kyoto Animation"
    elif(soup.find_all('a', title="J.C.Staff")):
        studio = "J.C. Staff"
    elif(soup.find_all('a', title="Madhouse")):
        studio = "Madhouse Inc."
    elif(soup.find_all('a', title="Wit Studio")):
        studio = "Wit Studio"
    elif(soup.find_all('a', title="Aniplex")):
        studio = "Aniplex"
    elif(soup.find_all('a', title="ADV Films")):
        studio = "ADV Films"
    elif(soup.find_all('a', title="Aniplex of America")):
        studio = "Aniplex of America"
    elif(soup.find_all('a', title="Bandai Visual")):
        studio = "Bandai Visual"
    elif(soup.find_all('a', title="Sunrise")):
        studio = "Sunrise"
    elif(soup.find_all('a', title="Manglobe")):
        studio = "Manglobe"
    elif(soup.find_all('a', title="Toei Animation")):
        studio = "Toei Animation"
    elif(soup.find_all('a', title="Studio Pierrot")):
        studio = "Studio Pierrot"
    elif(soup.find_all('a', title="Funimation")):
        studio = "Funimation"
    elif(soup.find_all('a', title="White Fox")):
        studio = "White Fox"
    elif(soup.find_all('a', title="TNK")):
        studio = "TNK"
    elif(soup.find_all('a', title="Lerche")):
        studio = "Lerche"
    elif(soup.find_all('a', title="Imagin")):
        studio = "Imagin"
    elif(soup.find_all('a', title="AIC Build")):
        studio = "AIC Build"
    elif(soup.find_all('a', title="TMS Entertainment")):
        studio = "TMS Entertainment"
    elif(soup.find_all('a', title="Nippon Animation")):
        studio = "Nippon Animation"
    else:
        studio = "Estudio nao listado"

    return studio
