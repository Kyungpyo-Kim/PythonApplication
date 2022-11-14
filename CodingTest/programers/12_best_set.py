# 프로그래머스 레벨3 최고의집합 연습문제

def solution(n, s):
    if n > s:
        return [-1]
    
    q = s // n
    r = s % n
    answer = []
    for _ in range(n):
        answer.append(q + 1 if r else q)
        if r:
            r -= 1
    answer.sort()
    return answer

if __name__ == "__main__":
    n = 2
    s = 9
    print(solution(n, s))

    n = 2
    s = 1
    print(solution(n, s))

    n = 2
    s = 8
    print(solution(n, s))