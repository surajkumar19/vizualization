# -*- coding: utf-8 -*-
"""
Created on Fri Dec 21 17:43:54 2018

@author: devar
"""

from requests import get
from bs4 import BeautifulSoup
import pandas as pd


url = 'https://www.imdb.com/search/title?title_type=feature&count=250&start='

response = get(url)
#print(response.text[:500])

html_soup = BeautifulSoup(response.text, 'html.parser')
movie_containers = html_soup.find_all('div', class_ = 'lister-item mode-advanced')


# Redeclaring the lists to store data in
names_popular = []
years_popular = []
imdb_ratings_popular = []
#metascores = []
votes_popular = []

# Redeclaring the lists to store data in
names_votes  = []
years_votes  = []
imdb_ratings_votes  = []
#metascores = []
votes_votes  = []  


headers = {"Accept-Language": "en-US, en;q=0.5"}

pages = [str(i) for i in range(1,1000, 250)]

count_1 = 0
count_2 = 0

for page in pages:
    
    if count_1 >=20 and count_2 >= 20:
        break
    
    # Make a get request
    response = get(url + page, headers = headers)
    
    # Parse the content of the request with BeautifulSoup
    page_html = BeautifulSoup(response.text, 'html.parser')
    
    # Select all the 50 movie containers from a single page
    mv_containers = page_html.find_all('div', class_ = 'lister-item mode-advanced')
    
    # For every movie of these 50
    for container in mv_containers:
        # If the movie has a Metascore, then:
        if container.find('div', class_ = 'ratings-metascore') is not None:
                        # Scrape the name
            name = container.h3.a.text
            
            # Scrape the year 
            year = container.h3.find('span', class_ = 'lister-item-year').text
            year = int(year[-5:-1])
            
            # Scrape the IMDB rating
            imdb = float(container.strong.text)
            
            # Scrape the number of votes
            vote = int(container.find('span', attrs = {'name':'nv'})['data-value'])
            
            if (imdb > 8) and (count_1 < 20 ):
                names_popular.append(name)
                years_popular.append(year)
                imdb_ratings_popular.append(imdb)
                votes_popular.append(int(vote))
                count_1 += 1
            
            if (vote > 40000) and (year >=2000) and (count_2 < 20 ):
            
                names_votes.append(name)
                years_votes.append(year)
                imdb_ratings_votes.append(imdb)
                votes_votes.append(int(vote))
                count_2 += 1


# =============================================================================


movie_ratings = pd.DataFrame({'movie': names_popular,
                              'year': years_popular,
                              'imdb': imdb_ratings_popular,
                              'votes': votes_popular})

movie_ratings = movie_ratings[['movie', 'year', 'imdb', 'votes']]
movie_ratings.to_csv('movie_popular.csv')


# =============================================================================

movie_ratings = pd.DataFrame({'movie': names_votes,
                              'year': years_votes,
                              'imdb': imdb_ratings_votes,
                              'votes': votes_votes})

movie_ratings = movie_ratings[['movie', 'year', 'imdb', 'votes']]
movie_ratings.to_csv('movie_votes.csv')
