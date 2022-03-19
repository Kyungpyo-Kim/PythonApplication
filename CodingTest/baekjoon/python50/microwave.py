t = int(input())

if t % 10 == 0:
    a = t // 300
    b = (t - 300*a) // 60
    c = (t - 300*a - 60*b) // 10
    print(a, b, c)
else:
    print(-1)