attendee = int(input())

price = list()
for i in range(attendee):
    a, b, c = sorted(map(int, input().split()))
    price.append(
        100*[c, 10+b, 100+10*b][[a,b,c].count(b)-1]
    )
print(max(price))