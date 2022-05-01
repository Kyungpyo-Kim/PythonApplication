import sys
input = sys.stdin.readline

n, k = map(int, input().split())
a, b = 1, 1

while k:
    a *= n
    b *= k
    n -= 1
    k -= 1

print(int(a/b)%10007)