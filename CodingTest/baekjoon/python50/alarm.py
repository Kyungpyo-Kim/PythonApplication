h, m = map(int, input().split())

t = h * 60 + m - 45
h = t // 60 % 24
m = t % 60

print(h, m)
