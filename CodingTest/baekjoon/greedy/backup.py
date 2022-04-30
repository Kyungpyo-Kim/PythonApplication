from queue import PriorityQueue
import sys
input = sys.stdin.readline

n, k = map(int, input().split())
com = [int(input()) for _ in range(n)]

visited = [False for _ in range(n)]

pque = PriorityQueue()
for i in range(1, len(com)):
    dist = com[i] - com[i - 1]
    pque.put((dist, (i - 1, i)))  # distance, left, right

dist_total = 0
for _ in range(k):
    while True:
        dist, (i, j) = pque.get()
        if not visited[i] and not visited[j]:
            break

    dist_total += dist
    visited[i], visited[j] = True, True

    if i > 0 and j + 1 < n:
        dist_right = com[j + 1] - com[j]
        dist_left = com[i] - com[i - 1]
        pque.put((dist_right + dist_left - dist, (i - 1, j + 1)))

print(dist_total)
