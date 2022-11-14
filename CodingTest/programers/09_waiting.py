# 프로그래머스 레벨3 선입선출스케쥴링 연습문제


def solution(n, cores):

    if n <= len(cores):
        return n

    n -= len(cores)
    left = 0
    right = n * max(cores)

    while left < right:
        mid = (left + right) // 2
        capacity = 0
        for c in cores:
            capacity += mid // c
        if capacity >= n:
            right = mid
        else:
            left = mid + 1

    for c in cores:
        n -= (right - 1) // c

    for i in range(len(cores)):
        if right % cores[i] == 0:
            n -= 1
            if n == 0:
                return i + 1


if __name__ == "__main__":
    n = 6
    cores = [1, 2, 3]
    print(solution(n, cores))
