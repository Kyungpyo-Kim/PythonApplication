from queue import PriorityQueue

# n, k = map(int, input().split())
# com = [int(input()) for _ in range(n)]

n, k = 5, 2
com = [1, 3, 4, 6, 12]

pque = PriorityQueue()
for i in range(1, len(com)):
    dist = com[i]-com[i-1]
    pque.put((dist, [i-1, i])) # distance, left, right

while n-1:
    print(pque.get())
    n -= 1
