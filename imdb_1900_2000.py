# -*- coding: utf-8 -*-
"""
Created on Fri Dec 21 17:43:54 2018

@author: devar
"""

from requests import get
from bs4 import BeautifulSoup
import pandas as pd


#url = 'https://www.imdb.com/search/title?title_type=feature&release_date=1999-01-01,1999-12-31&count=250'

#response = get(url)
#print(response.text[:500])

#html_soup = BeautifulSoup(response.text, 'html.parser')
#movie_containers = html_soup.find_all('div', class_ = 'lister-item mode-advanced')


# Redeclaring the lists to store data in
names = []
years = []
imdb_ratings = []
#metascores = []
votes = []




headers = {"Accept-Language": "en-US, en;q=0.5"}

#pages = [str(i) for i in range(2000,2018)]
pages=["2018"]


for page in pages:
    print(page)
    
    # Make a get request
    response = get("https://www.imdb.com/search/title?title_type=feature&release_date="+page+"-01-01,"+page+"-12-31&count=250", headers = headers)
    
    # Parse the content of the request with BeautifulSoup
    page_html = BeautifulSoup(response.text, 'html.parser')
    
    # Select all the 50 movie containers from a single page
    mv_containers = page_html.find_all('div', class_ = 'lister-item mode-advanced')
    
    # For every movie of these 50
    for container in mv_containers:
       
        # Scrape the name
        name = container.h3.a.text
        
        
        # Scrape the year 
        year = container.h3.find('span', class_ = 'lister-item-year').text
        year = int(year[-5:-1])
        
        # Scrape the IMDB rating
        try:
            imdb_rate = float(container.strong.text)
            
            # Scrape the number of votes
            vote = int(container.find('span', attrs = {'name':'nv'})['data-value'])
        except:
            continue
        names.append(name)
        years.append(year)
        imdb_ratings.append(imdb_rate)
        votes.append(int(vote))

# =============================================================================


movie_ratings = pd.DataFrame({'movie': names,
                              'year': years,
                              'imdb': imdb_ratings,
                              'votes': votes})

movie_ratings = movie_ratings[['movie', 'year', 'imdb', 'votes']]
movie_ratings.to_csv('movie_100_years_2.csv')



