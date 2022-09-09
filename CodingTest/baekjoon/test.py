""" test.py """
# import sys
# input = sys.stdin.readline
def solution():
    """solution"""
    _, target = map(int, input().split())
    arr = list(map(int, input().split()))

    # left bound
    low = 0
    high = int(1e9)

    while low + 1 < high:
        height = (low + high) // 2

        # [low, high] 범위 안에서 T, T, T, ... T, F, F, ... F
        # True 이면, low = height 로 업데이트
        total = sum([a - height for a in arr if a > height])
        if target <= total:
            low = height
        else:
            high = height

    print(low)


solution()
