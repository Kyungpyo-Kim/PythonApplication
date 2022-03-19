r = int(input())

c = s = 100
for _ in range(r):
    cd, sd = map(int, input().split())
    if cd > sd:
        s -= cd
    elif cd < sd:
        c -= sd
    else:
        pass
print(c, s, sep="\n")