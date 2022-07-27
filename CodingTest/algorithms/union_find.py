import sys

sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n, m = map(int, input().split())

parent = list(range(n + 1))


def find(a):
    if parent[a] == a:
        return parent[a]

    # path compression
    parent[a] = find(parent[a])
    return parent[a]


def union(a, b):
    a_parent = find(a)
    b_parent = find(b)
    new_parent = a_parent if a_parent < b_parent else b_parent
    parent[a_parent] = parent[b_parent] = new_parent


def check(a, b):
    if find(a) == find(b):
        print("yes")
    else:
        print("no")


for _ in range(m):
    op, a, b = map(int, input().split())
    if op == 0:
        union(a, b)
    else:
        check(a, b)
