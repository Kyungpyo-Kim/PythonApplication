# O(NloglogN)
m, n = map(int, input().split())

rt = int(n**0.5) + 1

sieve = [False, False] + [True] * (n - 1)

for i in range(2, rt + 1):
    if sieve[i]:
        for j in range(i*2, n+1, i):
            sieve[j] = False

for i in range(m, n + 1):
    if sieve[i]:
        print(i)