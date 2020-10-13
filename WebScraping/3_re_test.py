import re

p = re.compile('ca.e')
## .: 하나의 문자를 의미
## ^: 문자열의 시작
## $: 문자열의 끝

def print_match(m):
  if m:
    print("일치하는 문자열 m.group()", m.group()) 
    print("입력받은 문자열 m.string", m.string)
    print("일치하는 문자열의 시작 index m.start()", m.start()) 
    print("일치하는 문자열의 끝 index m.end()", m.end())
    print("일치하는 문자열의 시작/끝 index m.span()", m.span())
  else:
    print("no matching")

## match: 문자열의 처음부터 일치하는지 확인
m = p.match("cafe")
print_match(m)

m = p.match("caffe")
print_match(m)

m = p.match("careless")
print_match(m)

## search: 문자열 중에 일치하는게 있는지 확인
m = p.search("good care")
print_match(m)

## findall: 일치하는 모든 것을 리스트 형태로 반환
l = p.findall("careless, good care cafe")
print(l)