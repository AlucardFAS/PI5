# PI5 - Machine Learning

The main repository is at https://github.com/AlucardFAS/PI5

<H1>Author</h1>

Fernando Silva</br>
Victor Trindade</br>
Danilo Mative</br>

<h2> Web Scraping </h2>

O Web Scraping nomeado como <a href="https://github.com/AlucardFAS/PI5/blob/master/PI%20V/Projeto%20Final/animeSearch/search.py">search.py</a> utiliza o módulo <a href="https://github.com/AlucardFAS/PI5/blob/master/PI%20V/Projeto%20Final/animeSearch/searchStudio.py">searchStudio.py</a> e <a href="https://github.com/AlucardFAS/PI5/tree/master/PI%20V/Projeto%20Final/animeSearch/bs4">BeautifulSoup 4</a> para realizar uma busca em cada página do Website <a href="https://myanimelist.net/">MyAnimeList</a> e carregar todo o código fonte, separando e salvando uma série de dados de cada anime.</br></br>
Web Scraping named as search.py uses the searchStudio.py and BeautifulSoup 4 module to perform a search on each page of the MyAnimeList Website and load all the source code, separating and saving a series of data from each anime.</br>

<h2>Output</h2>

A saída contém um .txt separado em vírgulas com o nome test, que contém os seguintes parâmetros: ID, Status de lançamento, Produtora, Estúdio, Fonte, Gênero 1, Gênero 2, Gênero 3, Duração, Classificação Indicativa, Episódios, Nota.</br></br>
The output contains a comma separated .txt with the following parameters: ID, Release Status, Producer, Studio, Source , Genre 1, Genre 2, Genre 3, Duration, Indicative Rating, Episodes, Note.</br>

<h3>
<a href="https://github.com/AlucardFAS/PI5/blob/master/PI%20V/Projeto%20Final/animeSearch/myanimelist.txt">Example Output</a>
</h3>

<h2>Exception</h2>

O código lança exceções para notfound 404 e animes com dados incompletos.</br></br>
The code throws exceptions for notfound 404 and animes with incomplete data.</br>
