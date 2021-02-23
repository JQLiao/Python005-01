import requests
from bs4 import BeautifulSoup as bs
import csv

user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.103 Safari/537.36"

header = {'user-agent':user_agent}

doubanurl = "https://maoyan.com/board"

response = requests.get(doubanurl, headers=header)

# print(response.text)
print(f'返回的状态码：{response.status_code}')

bs_info = bs(response.text, 'html.parser')

with open('movie_top10.csv','w', encoding='utf-8') as csvfile:
    fieldnames = ['name','star','releasetime']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    movie = {}
    for tags in bs_info.find_all('div', attrs={'class': 'board-item-content'}):
        movie["name"] = tags.a['title']
        movie["star"] = tags.find('p', attrs={'class': 'star'}).text.strip()
        movie["releasetime"] = tags.find('p', attrs={'class': 'releasetime'}).text.strip().split('：')[1]
        writer.writerow(movie)

