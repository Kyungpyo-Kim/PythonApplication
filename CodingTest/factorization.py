N = int(input())
i = 2
r = int(N ** 0.5)

while i <= r:
    while not N % i:
        print(i)
        N //= i
    i += 1
    if N == 1:
        break

if N > 1:
    print(N)