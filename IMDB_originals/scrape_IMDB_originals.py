from bs4 import BeautifulSoup
import requests
import pandas as pd

try:
    HEADER = {
        'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'}
    URL = "https://www.imdb.com/"
    PROXY = {"http": "http//80.48.119.28:8080"}

    response = requests.get(URL, proxies=PROXY, headers=HEADER)
    page_html = response.text

    soup = BeautifulSoup(page_html, 'html.parser')
    # print(soup)

    shows = soup.find('div', class_='ipc-sub-grid ipc-sub-grid--page-span-3 ipc-sub-grid--nowrap '
                                    'ipc-sub-grid--4-unit-at-s ipc-shoveler__grid').find_all('div', class_='ipc-slate'
                                                                                                           '-card__text-container')

    # print(shows)
    name_list = []

    for show in shows:

        name = show.find('div', class_='ipc-slate-card__title-text ipc-slate-card__title-text--clamp-none').text
        name_list.append(name)

        # print(name)

    details_dict = {'IMDB Originals': name_list}

    output = pd.DataFrame(details_dict)
    output.to_csv("/home/ayushi/Desktop/IMDB_originals_data.csv", index=False)


except Exception as e:
    print(e)
