# 프로그래머스 레벨3 코딩테스트공부 2022카카오테크인턴쉽

huge_val = 1000000007


def solution(alp, cop, problems):
    target_alp, target_cop = alp, cop
    for problem in problems:
        target_alp = max(problem[0], target_alp)
        target_cop = max(problem[1], target_cop)

    alp = min(alp, target_alp)
    cop = min(cop, target_cop)

    dp = [[huge_val for _ in range(target_cop + 1)] for _ in range(target_alp + 1)]
    dp[alp][cop] = 0
    for cur_alp in range(alp, target_alp + 1):
        for cur_cop in range(cop, target_cop + 1):
            if cur_alp + 1 <= target_alp:
                dp[cur_alp + 1][cur_cop] = min(
                    dp[cur_alp + 1][cur_cop], dp[cur_alp][cur_cop] + 1
                )
            if cur_cop + 1 <= target_cop:
                dp[cur_alp][cur_cop + 1] = min(
                    dp[cur_alp][cur_cop + 1], dp[cur_alp][cur_cop] + 1
                )
            for alp_req, cop_req, alp_rwd, cop_rwd, cost in problems:
                if cur_alp >= alp_req and cur_cop >= cop_req:
                    new_alp = min(target_alp, cur_alp + alp_rwd)
                    new_cop = min(target_cop, cur_cop + cop_rwd)
                    dp[new_alp][new_cop] = min(
                        dp[new_alp][new_cop],
                        dp[cur_alp][cur_cop] + cost,
                    )
    return dp[target_alp][target_cop]


if __name__ == "__main__":
    alp = 10
    cop = 10
    problems = [[10, 15, 2, 1, 2], [20, 20, 3, 3, 4]]
    print(solution(alp, cop, problems))

    alp = 0
    cop = 0
    problems = [[0, 0, 2, 1, 2], [4, 5, 3, 1, 2], [4, 11, 4, 0, 2], [10, 4, 0, 4, 2]]
    print(solution(alp, cop, problems))
