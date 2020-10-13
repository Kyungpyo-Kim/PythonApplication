# WebScraping
* [reference](https://www.youtube.com/watch?v=yQ20jZwDjTE)
* [W3schools](w2schools.com)
  - html
  - python regular expression

* Web Scraping
  - 원하는 부분만
* Web Crawling
  - 모두 가져오기

## Web
* HTML - 구조
* CSS - 인테리어
* JAVA Script - 동적

## Xpath

## Reqests
```bash
pip3 install requests
python3 3_re_test.py
```

## Regular Expressions

## User-agent
* https://www.whatismybrowser.com/detect/what-is-my-user-agent
```python
import requests
url = "http"
headers = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Whale/2.8.105.18 Safari/537.36"}
res = requests.get(url, headers=headers)
res.raise_for_status()
```

## BeautifulSoup4
```bash
pip3 install beautifulsoup4
pip3 install lxml
python3 4_bs4.py
```

## HTTP Method
* Get
  - Web 주소 ? 뒤에 있는 변수, 값을 넘겨 보낸다. (페이지를 요청한다.) 
  - 큰 데이터는 보내기 어렵다.
  - 데이터 보안이 어렵다.
* Post
  - 큰 데이터, 보안이 필요한 데이터를 보낼때 사용한다.
  - page 는 그대로인데 내용이 바뀌는 경우가 post 방식을 사용

