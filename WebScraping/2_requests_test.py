import requests

# res = requests.get("http://naver.com")
# print ( "status code: ", res.status_code) 
## res.status_code == 200, normal
## res.status_code == 403, no athourithm
# if res.status_code == requests.codes.ok:
#   print ( "normal")
# else:
#   print ( "problem, [error code: ", res.status_code, "]")
# res = requests.get("http://kyungpyo.com")
# res.raise_for_status()
# print ("start scraping")

res = requests.get("http://google.com")
res.raise_for_status()
print ( len(res.text) )

with open("mygoogle.html", "w", encoding="utf8") as f:
  f.write(res.text)