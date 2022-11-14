# 프로그래머스 레벨3 섬연결하기 그리디

def solution(n, costs):
    costs.sort(key=lambda x: x[2])
    routes = set([costs[0][0]])
    answer = 0

    while len(routes) < n:
        for i, cost in enumerate(costs):
            if cost[0] in routes and cost[1] in routes:
                continue
            if cost[0] in routes or cost[1] in routes:
                routes.update([cost[0], cost[1]])
                answer += cost[2]
                costs[i] = [-1, -1, -1]
                break
    return answer


if __name__ == "__main__":
    n = 4
    costs = [[0,1,1],[0,2,2],[1,2,5],[1,3,1],[2,3,8]]
    print(solution(n, costs))