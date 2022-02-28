# a, b, c = map(int, input().split())

# if a == b == c:
#     print(a * 1000 + 10000)
# elif a==b or b==c or c==a:
#     if a==b:
#         print(a * 100 + 1000)
#     elif b==c:
#         print(b * 100 + 1000)
#     elif c==a:
#         print(c * 100 + 1000)
# else:
#     print(max([a,b,c])*100)

a, b, c = sorted(map(int, input().split()))
print([c,b+10,b*10+100][[a,b,c].count(b)-1]*100)