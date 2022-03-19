a1, b1 = map(int, input().split())
a2, b2 = map(int, input().split())
a3, b3 = map(int, input().split())

if a1 == a2:
    a = a3
elif a1 == a3:
    a = a2
else:
    a = a1

if b1 == b2:
    b = b3
elif b1 == b3:
    b = b2
else:
    b = b1
print(a, b)