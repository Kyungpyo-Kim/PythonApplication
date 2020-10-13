import requests
from bs4 import BeautifulSoup
import re


headers = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Whale/2.8.105.18 Safari/537.36"}

for i in range(1, 5):
  print("Page: {}".format(i))
  url = 'https://www.coupang.com/np/search?q=notebook&channel=user&component=&eventCategory=SRP&trcid=&traid=&sorter=scoreDesc&minPrice=&maxPrice=&priceRange=&filterType=&listSize=36&filter=&isPriceRange=false&brand=&offerCondition=&rating=0&page={}&rocketAll=false&searchIndexingToken=1=4&backgroundColor='.format(i)
  res = requests.get(url, headers=headers)
  res.raise_for_status()

  soup = BeautifulSoup(res.text, 'lxml')

  items = soup.find_all('li', 
    attrs={"class":re.compile("^search-product")})

  for item in items:
    
    ## Exclude elements with ad_badge
    ad_badge = item.find("span", attrs={"class":"ad-badge-text"})
    if ad_badge:
      continue

    ## Exclude Apple product
    name = item.find('div', attrs={'class':'name'}).get_text() ## product name
    if 'Apple' in name:
      continue

    price = item.find('strong', attrs={'class':'price-value'}).get_text() ## price
    
    ## Include elements larger than 4.5 rate
    rate = item.find('em', attrs={'class':'rating'}) ## rating
    if rate:
      rate = rate.get_text()
    else:
      rate = "No rate"
      continue
    if float(rate) <= 4.5:
      continue
    
    ## Include elements larger than 100 count
    rate_cnt = item.find('span', attrs={'class':'rating-total-count'}) ## count of rating
    if rate_cnt:
      rate_cnt = rate_cnt.get_text()
    else:
      rate_cnt = "No rate cnt"
      continue
    if int(rate_cnt[1:-1]) <= 100:
      continue
    
    link = item.find('a', attrs={'class':'search-product-link'})['href']

    print("-"*80)
    print("name:", name)
    print("price:", price)
    print("rate:", rate)
    print("rate_cnt:", rate_cnt)
    print("link: https://www.coupang.com{}".format(link))