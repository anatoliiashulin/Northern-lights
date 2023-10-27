from bs4 import BeautifulSoup
import requests

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36"} 

SITE = 'https://pogoda.mail.ru/prognoz/sankt_peterburg/'

response = requests.get(SITE, headers=headers)
soup = BeautifulSoup(response.text, 'lxml')

data = []

day_0 = soup.find_all('div', class_='information__content__additional__item')
data.append(day_0[2].text.replace('\t', '').replace('\n', ''))

week = soup.find('div', class_='cols__column__inner')
week = week.find_all('div', class_='day day_index')

for i in week:
    data.append(i.find_all('div')[1].get('title'))



if __name__ == '__main__':
    for i, j in enumerate(data):
        print(f'день {i}, погода = {j}')