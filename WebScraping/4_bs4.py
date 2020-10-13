import requests
from bs4 import BeautifulSoup

url = "https://comic.naver.com/index.nhn"
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml")
print(soup.title)
print(soup.title.get_text())
print(soup.a) ## soup 객체에서 처음 발견되는 a element
print(soup.a.attrs) ## a element의 속성 정보
print(soup.a['href']) ## a element의 href 정보

print(soup.find('a', attrs={"class": "Nbtn_upload"})) ## class = "Nbtn_upload" 인 a element
print(soup.find(attrs={"class": "Nbtn_upload"})) ## class = "Nbtn_upload"

rank2 = soup.find("li", attrs={"class":"rank02"})
print(rank2.a.get_text())
print(rank2.previous_sibling)
print(rank2.next_sibling)
print(rank2.parent)
print(rank2.find_next_sibling('li').a.get_text())
print(rank2.find_previous_sibling('li').a.get_text())
print(rank2.find_next_siblings("li"))

webtoon = soup.find('a', text='이번 생도 잘 부탁해-18화')
print(webtoon)