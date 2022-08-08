import pandas as pd
from bs4 import BeautifulSoup
import requests

try:
    HEADER = {
        'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'}
    URL = "https://www.imdb.com/showtimes/location?ref_=sh_lc"
    PROXY = {"http": "http//80.48.119.28:8080"}

    response = requests.get(URL, proxies=PROXY, headers=HEADER)
    page_html = response.text

    soup = BeautifulSoup(page_html, 'html.parser')

    shows = soup.find('div', class_='lister-list').find_all('div', class_='lister-item mode-grid')
    # print(shows)
    # print(len(shows))

    rank_list = []
    name_list = []
    year_list = []
    director_list = []

    for show in shows:

        rank = show.find('div', class_='posterInfo').strong.text.strip()
        rank_list.append(rank)

        name = show.find('div', class_='title').a.text
        name_list.append(name)

        year = show.find('h3', class_='lister-item-header').span.text.strip('()')
        year_list.append(year)

        director = show.find_next('p', class_='text-muted text-small').find_next('p',
                                                                                 class_='text-muted text-small').a.text
        director_list.append(director)

    details_dict = {'Movie Rank': rank_list,
                    'Movie Name': name_list,
                    'Movie Year': year_list,
                    'Movie Director': director_list}

    output = pd.DataFrame(details_dict)
    output.to_csv("/home/ayushi/Desktop/IMDB_movies_TV_shows_data.csv", index=False)

except Exception as e:
    print(e)
