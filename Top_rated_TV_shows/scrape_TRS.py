from bs4 import BeautifulSoup
import requests
import pandas as pd

try:
    source = requests.get('https://www.imdb.com/chart/toptv/')
    source.raise_for_status()

    soup = BeautifulSoup(source.text, 'html.parser')

    shows = soup.find('tbody', class_='lister-list').find_all('tr')

    rank_list = []
    name_list = []
    year_list = []
    rating_list = []

    for show in shows:
        rank = show.find('td', class_='titleColumn').get_text(strip=True).split('.')[0]
        rank_list.append(rank)

        name = show.find('td', class_='titleColumn').a.text
        name_list.append(name)

        year = show.find('td', class_='titleColumn').span.text.strip('()')
        year_list.append(year)

        rating = show.find('td', class_='ratingColumn imdbRating').strong.text
        rating_list.append(rating)

    output_dict = {'Show Rank': rank_list,
                   'Show Name': name_list,
                   'Show Year': year_list,
                   'IMDB Ratings': rating_list}

    output = pd.DataFrame(output_dict)
    output.to_csv("/home/ayushi/Desktop/IMDB_TRS_data.csv", index=False)

except Exception as e:
    print(e)
