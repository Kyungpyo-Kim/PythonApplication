import requests
from bs4 import BeautifulSoup

url = "https://comic.naver.com/webtoon/list.nhn?titleId=748105&weekday=thu"
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, 'lxml')
cartoons = soup.find_all('td', attrs={'class':'title'})

for c in cartoons:
  print(c.a.get_text(), "https://comic.naver.com"+c.a['href'])

sum_strong = 0
strongs = soup.find_all('div', attrs={'class':'rating_type'})
for s in strongs:
  sum_strong += float( s.find('strong').get_text() )

print('total:', sum_strong)
print('avg:', sum_strong/len(strongs))