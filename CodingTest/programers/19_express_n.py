# 프로그래머스 레벨3 N으로 표현 동적프로그래밍
from collections import defaultdict

def solution(N, number):
    if N == number:
        return 1
    table = defaultdict(set)
    table[1].add(N)
    for i in range(2, 9):
        table[i].add(int(str(N) * i))
        for j in range(1, i):
            for x in table[j]:
                for y in table[i-j]:
                    table[i].add(x + y)
                    table[i].add(x - y)
                    table[i].add(x * y)
                    if y != 0:
                        table[i].add(x // y)
        if number in table[i]:
            return i
    return -1



if __name__ == "__main__":
    N = 5
    number = 12
    print(solution(N, number))
    N = 2
    number = 11
    print(solution(N, number))
