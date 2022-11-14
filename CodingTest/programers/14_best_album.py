# 프로그래머스 레벨3 베스트앨범 해시
from collections import defaultdict
import heapq


def solution(genres, plays):
    size = len(genres)
    table = defaultdict(list)
    cnt = defaultdict(int)
    for i in range(size):
        table[genres[i]].append((-plays[i], i))
        cnt[genres[i]] += plays[i]

    q_genres = []
    for key in table:
        heapq.heappush(q_genres, (-cnt[key], key))
        heapq.heapify(table[key])

    answer = []
    for _ in range(len(table)):
        key = heapq.heappop(q_genres)[1]
        for _ in range(2):
            if table[key]:
                answer.append(heapq.heappop(table[key])[1])
    return answer


if __name__ == "__main__":
    genres = ["classic", "pop", "classic", "classic", "pop"]
    plays = [500, 600, 150, 800, 2500]
    print(solution(genres, plays))
