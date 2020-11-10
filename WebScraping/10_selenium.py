from selenium import webdriver

browser = webdriver.Firefox(executable_path='./geckodriver')
browser.get("http://naver.com")

"""
>>> browser = webdriver.Firefox(executable_path='./geckodriver')
>>> browser.get("http://naver.com")
>>> elem = browser.find_element_by_class_name("link_login")
>>> elem.click()
>>> browser.back()
b>>> browser.forward()
>>> browser.refresh()
>>> browser.back()
>>> elem = browser.find_element_by_id("query")
>>> elem
<selenium.webdriver.firefox.webelement.FirefoxWebElement (session="20b7ae83-df05-4690-a7d2-6ea28afa003c", element="5f894e11-4944-4bd4-9d6a-1afed48d3953")>
>>> from selenium.webdriver.common.keys import Keys
>>> elem.send_keys("나도코딩")
>>> elem.send_keys(Keys.ENTER)
>>> elem = browser.find_elements_by_tag_name("a")
>>> for e in elem:
...   e.get_attribute("href")
...   break
... 
'https://search.naver.com/search.naver?sm=top_hty&fbm=0&ie=utf8&query=%EB%82%98%EB%8F%84%EC%BD%94%EB%94%A9#lnb'
"""
