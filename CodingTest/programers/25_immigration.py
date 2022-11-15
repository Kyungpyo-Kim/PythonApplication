# 프로그래머스 레벨3 입국심사 이분탐색

def solution(n, times):
    left = 1
    right = max(times) * n
    def check(time):
        return sum([time // t for t in times])

    while left < right:
        mid = (left + right) // 2
        if check(mid) < n:
            left = mid + 1
        else:
            right = mid

    return left


if __name__ == "__main__":
    n = 6
    times = [7, 10]
    print(solution(n, times))