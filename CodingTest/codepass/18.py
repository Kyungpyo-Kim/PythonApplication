import sys

input = sys.stdin.readline

W, H = map(int, input().strip().split())

arr = [input().strip() for _ in range(H)]

C = int(input())

if C == 0:
    W, H = H, W
    new_arr = [[0] * W for _ in range(H)]
    for w in range(W):
        for h in range(H):
            new_arr[h][w] = arr[W - w - 1][h]
    arr = new_arr

if C == 1:
    new_arr = [[0] * W for _ in range(H)]
    for w in range(W):
        for h in range(H):
            new_arr[h][w] = arr[H - h - 1][W - w - 1]
    arr = new_arr

if C == 2:
    W, H = H, W
    new_arr = [[0] * W for _ in range(H)]
    for w in range(W):
        for h in range(H):
            new_arr[h][w] = arr[w][H - h - 1]
    arr = new_arr

if C == 3:
    new_arr = [[0] * W for _ in range(H)]
    for w in range(W):
        for h in range(H):
            new_arr[h][w] = arr[H - h - 1][w]
    arr = new_arr

if C == 4:
    new_arr = [[0] * W for _ in range(H)]
    for w in range(W):
        for h in range(H):
            new_arr[h][w] = arr[h][W - w - 1]
    arr = new_arr

print(f"{W} {H}")
for h in range(H):
    for w in range(W):
        print(arr[h][w], end="")
    print()
