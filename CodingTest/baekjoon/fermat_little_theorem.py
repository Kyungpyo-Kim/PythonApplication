'''
answer = (n!/(k!(n-k)!))%p
       = (n!%p x (k!(n-k)!)^(-1)%p)%p
       = (n!%p x (k!(n-k)!)^(p-2)%p)%p

a = k!(n-k)!
p = 1000000007

Fermat's Little Theorem
  a%p x a^(p-2)%p = 1
'''

p = 1000000007
dp = [0]*40000000
dp[0] = 1
dp[1] = 1
def factorial(n):
    global dp
    for i in range(2, n+1):
        if dp[i] == 0:
            dp[i] = i * dp[i-1] % p
    return dp[n]

def pow(a, b):
    ret = 1
    while b > 0:
        if b % 2 == 1:
            ret *= a
            ret %= p
        a *= a
        a %= p
        b //= 2
    return ret

n, k = map(int, input().split())
print((factorial(n) * pow(factorial(k) * factorial(n-k), p-2))%p)