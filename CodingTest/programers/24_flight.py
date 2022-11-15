# 프로그래머스 레벨3 여행결로 깊이너비우선탐색
def solution(tickets):
    tickets.sort()
    start = "ICN"
    path = [start]
    answer = None
    visited = set()
    def dfs(start):
        if len(visited) == len(tickets):
            nonlocal answer
            answer = path[:]
            return
        for i, ticket in enumerate(tickets):
            if ticket[0] == start and i not in visited:
                visited.add(i)
                path.append(ticket[1])
                dfs(ticket[1])
                if answer:
                    return
                visited.remove(i)
                path.pop()
        return
    
    dfs(start)
    return answer

if __name__ == "__main__":
    tickets = [["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]
    print(solution(tickets))

    tickets = [["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]
    print(solution(tickets))