# 프로그래머스 레벨3 가장긴펠렌드롬 연습문제

def solution(s):
    answer = 0
    # get length of longest palindrome
    for i in range(len(s)):
        for j in range(i + 1, len(s) + 1):
            if s[i:j] == s[i:j][::-1]:
                answer = max(answer, len(s[i:j]))
    return answer

if __name__ == "__main__":
    s = "abcdcba"
    print(solution(s))
    s = "abacde"
    print(solution(s))