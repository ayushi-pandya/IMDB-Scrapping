from bs4 import BeautifulSoup
import requests
import pandas as pd

try:
    HEADER = {
        'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'}
    URL = "https://www.imdb.com/chart/top/"
    PROXY = {"http": "http//80.48.119.28:8080"}

    response = requests.get(URL, proxies=PROXY, headers=HEADER)
    page_html = response.text

    soup = BeautifulSoup(page_html, 'html.parser')

    movies = soup.find('tbody', class_='lister-list').find_all('tr')
    # print(len(movies))

    rank_list = []
    name_list = []
    year_list = []
    rating_list = []

    for movie in movies:
        rank = movie.find('td', class_='titleColumn').get_text(strip=True).split('.')[0]
        rank_list.append(rank)

        name = movie.find('td', class_='titleColumn').a.text
        name_list.append(name)

        year = movie.find('td', class_='titleColumn').span.text.strip('()')
        year_list.append(year)

        rating = movie.find('td', class_='ratingColumn imdbRating').strong.text
        rating_list.append(rating)

        # print(rank, name, year, rating)
    details_dict = {'Movie Rank': rank_list,
                    'Movie Name': name_list,
                    'Movie Year': year_list,
                    'IMDB Ratings': rating_list}

    output = pd.DataFrame(details_dict)
    output.to_csv("/home/ayushi/Desktop/IMDB_TRM_data.csv", index=False)

except Exception as e:
    print(e)
