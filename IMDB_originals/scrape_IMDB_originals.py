from bs4 import BeautifulSoup
import requests
import pandas as pd

try:
    source = requests.get('https://www.imdb.com/')
    source.raise_for_status()

    soup = BeautifulSoup(source.text, 'html.parser')
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
