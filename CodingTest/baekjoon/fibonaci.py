import sys

input = sys.stdin.readline
mod = 1000000007
n = int(input())

def matMul(m1, m2):
    rank = len(m1)
    ret = [[0 for _ in range(rank)] for _ in range(rank)]
    for i in range(rank):
        for j in range(rank):
            for k in range(rank):
                ret[i][j] += m1[i][k] * m2[k][j]
            ret[i][j] %= mod
    return ret

def matPow(base, exp):
    rank = len(base)
    res = [[int(i==j) for i in range(rank)] for j in range(rank)]

    while exp > 1:
        if exp % 2 == 1:
            res = matMul(res, base)
        base = matMul(base, base)
        exp //= 2
    
    return matMul(res, base)
      
mat = [[1, 1], [1, 0]] 
print(matPow(mat, n)[0][1]) 