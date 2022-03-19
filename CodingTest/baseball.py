test_case = int(input())

for _ in range(test_case):
    total_y = total_k = 0
    for _ in range(9):
        y, k = map(int, input().split())
        total_y+= y
        total_k += k
    if total_y > total_k:
        print("Yonsei")
    elif total_k < total_k:
        print("Korea")
    else:
        print("Draw")