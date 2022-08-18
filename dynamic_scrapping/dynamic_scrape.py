import argparse

from bs4 import BeautifulSoup
import requests
import pandas as pd

try:

    HEADER = {
        'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'}

    parser = argparse.ArgumentParser()
    parser.add_argument("genres", default='action', help="path to the input image")
    parser.add_argument("sort", default='user_rating', help="path to the input image")
    parser.add_argument("desc", default='feature', help="path to the input image")
    parser.add_argument("vote", default='200', help="path to the input image")
    parser.add_argument('--genres', help='foo help')

    args = parser.parse_args()

    # genres = 'adventure'
    # sort = 'user_rating'
    # desc = 'feature'
    # vote = '100'

    URL = "https://www.imdb.com/search/title/?genres={genres}&sort={sort},desc&title_type={desc}&num_votes={vote}".format(
        genres=args.genres, sort=args.sort, desc=args.desc, vote=args.vote)
    print('url:', URL)
    PROXY = {"http": "http//80.48.119.28:8080"}

    response = requests.get(URL, proxies=PROXY, headers=HEADER)
    page_html = response.text

    soup = BeautifulSoup(page_html, 'html.parser')
    data = soup.find('div', class_='lister list detail sub-list').find_all('div', class_='lister-item-content')

    name_list = []

    for item in data:
        name = item.find('h3', class_='lister-item-header').a.text
        name_list.append(name)
        print(name)

    details_dict = {'Movie': name_list}

    output = pd.DataFrame(details_dict)
    output.to_csv("/home/ayushi/Desktop/search_data.csv", index=False)


except Exception as e:
    print(e)

