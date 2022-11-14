# 프로그래머스 레벨3 거스름돈 연습문제
def solution(n, money):
    dp = [0 for _ in range(n+1)]
    for m in money:
        dp[m] += 1
        for i in range(m+1, n+1):
            dp[i] += dp[i-m]
    return dp[n]

if __name__ == "__main__":
    n = 5
    money = [1, 2, 5]
    print(solution(n, money))