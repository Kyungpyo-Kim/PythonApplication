# 프로그래머스 레벨3 카운트다운 연습문제
huge_val = 1000000007
score_prime = set(i for i in range(1, 21))
score_prime.add(50)
score_second = set()
for i in range(1, 21):
    for j in range(2, 4):
        score_second.add(i * j)

dp = [[huge_val, 0] for _ in range(100001)]
dp[0] = [0,0]

def solution(target):
    for cnt in range(1, target + 1):
        for prime in score_prime:
            if cnt - prime >= 0:
                tmp_try = dp[cnt - prime][0] + 1
                tmp_cnt = dp[cnt - prime][1] + 1
                
                if tmp_try <= dp[cnt][0]:
                    dp[cnt] = [tmp_try, tmp_cnt]
        
        for second in score_second:
            if cnt - second >= 0:
                tmp_try = dp[cnt - second][0] + 1
                tmp_cnt = dp[cnt - second][1]
                
                if tmp_try < dp[cnt][0]:
                    dp[cnt] = [tmp_try, tmp_cnt]
                if tmp_try == dp[cnt][0]:
                    dp[cnt][1] = max(dp[cnt][1], tmp_cnt)

    answer = dp[target]
    return answer


if __name__ == "__main__":
    target = 21
    print(solution(target))
    target = 24
    print(solution(target))
    target = 58
    print(solution(target))