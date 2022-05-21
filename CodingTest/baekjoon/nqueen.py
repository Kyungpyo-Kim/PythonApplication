import sys

input = sys.stdin.readline

n = int(input())

ans = 0
queens = [0]*n
visited = [False]*n
def promising(x):
    for i in range(x):
        if queens[x] == queens[i]:
            return False
        if abs(queens[x]-queens[i]) == abs(x-i):
            return False
    return True

def n_queens(x):
    global ans, queens

    if x == n:
        ans += 1
        return

    for i in range(n):
        if visited[i]:
            continue
        queens[x] = i
        if promising(x):
            visited[i] = True
            n_queens(x+1)
            visited[i] = False

n_queens(0)
print(ans)