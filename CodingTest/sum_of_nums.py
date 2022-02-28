S = int(input())
i = 1
while S != 0:
    S = S-i

    if S <= i:
        break

    i += 1
print(i)