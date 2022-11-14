# 프로그래머스 레벨3 단어변환 깊이너비우선탐색
from collections import defaultdict, deque

def solution(begin, target, words):
    if target not in words:
        return 0

    q = deque([[begin, 0]])
    visited = set()

    def check(a, b):
        cnt = 0
        for i, j in zip(a, b):
            if i != j:
                cnt += 1
        return cnt == 1
        
    while q:
        node, depth = q.popleft()
        visited.add(node)

        child = [word for word in words if check(node, word)]
        for word in child:
            if word == target:
                return depth + 1
            if word not in visited:
                visited.add(word)
                q.append([word, depth + 1])
    
    return 0
    # if begin not in words:
    #     words = [begin] + words
    
    # word_len = len(words[0])
    # graph = defaultdict(list)
    # for i in range(len(words)):
    #     for j in range(i+1, len(words)):
    #         if len(set(list("".join([words[i], words[j]])))) == word_len + 1:
    #             graph[i].append(j)
    #             graph[j].append(i)

    # pq = deque()
    # visited = set()
    # huge_val = 10000000
    # dist_map = [huge_val for _ in range(len(words))]

    # for i in range(len(words)):
    #     if words[i] == begin:
    #         pq.append(i)
    #         dist_map[i] = 0
    
    # while pq:
    #     i = pq.popleft()
    #     visited.add(i)
    #     children = [j for j in graph[i] if j not in visited]
        
    #     for child in children:
    #         if child not in visited and dist_map[child] > dist_map[i] + 1:
    #             visited.add(child)
    #             dist_map[child] = dist_map[i] + 1
    #             pq.append(child)
    
    # for i in range(len(words)):
    #     if words[i] in target and dist_map[i] != huge_val:
    #         return dist_map[i]
    # return 0


if __name__ == "__main__":
    # begin = "hit"
    # target = "cog"
    # words = ["hot", "dot", "dog", "lot", "log", "cog"]
    # print(solution(begin, target, words))

    begin = "hit"
    target = "cog"
    words = ["hit", "hot", "dot", "dog", "lot", "log", "cog"]
    print(solution(begin, target, words))