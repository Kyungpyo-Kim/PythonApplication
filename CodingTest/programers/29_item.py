# 프로그래머스 레벨3 아이템줍기 깊이너비우선탐색
from collections import deque

def solution(rectangle, characterX, characterY, itemX, itemY):
    max_size = 51
    map = [[0 for _ in range(max_size)] for _ in range(max_size)]
    for rect in rectangle:
        for i in range(2*rect[0], 2*rect[2] + 1):
            for j in range(2*rect[1], 2*rect[3] + 1):
                if i == 2*rect[0] or j == 2*rect[1] or i == 2*rect[2] or j == 2*rect[3]:
                    if map[i][j] == 0:
                        map[i][j] = 1
                else:
                    map[i][j] = 2
        
    def bfs(start, end):
        queue = deque()
        queue.append(start)
        max_dist = 51**2
        dist = [[max_dist for _ in range(max_size)] for _ in range(max_size)]
        dist[start[0]][start[1]] = 0
        while queue:
            x, y = queue.popleft()
            if x == end[0] and y == end[1]:
                return dist[x][y]
            for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < max_size and 0 <= ny < max_size:
                    if map[nx][ny] == 1:
                        if dist[nx][ny] > dist[x][y] + 1:
                            dist[nx][ny] = dist[x][y] + 1
                            queue.append((nx, ny))
        return -1

    return bfs((characterX*2, characterY*2), (itemX*2, itemY*2))//2

if __name__ == "__main__":

    ractangle = [[1,1,7,4],[3,2,5,5],[4,3,6,9],[2,6,8,8]]
    characterX = 1
    characterY = 3
    itemX = 7
    itemY = 8
    print(solution(ractangle, characterX, characterY, itemX, itemY))

    ractangle = [[1,1,8,4],[2,2,4,9],[3,6,9,8],[6,3,7,7]]
    characterX = 9
    characterY = 7
    itemX = 6
    itemY = 1
    print(solution(ractangle, characterX, characterY, itemX, itemY))

    ractangle = [[1,1,5,7]]
    characterX = 1
    characterY = 1
    itemX = 4
    itemY = 7
    print(solution(ractangle, characterX, characterY, itemX, itemY))

    ractangle = [[2,1,7,5],[6,4,10,10]]	
    characterX = 3
    characterY = 1
    itemX = 7
    itemY = 10
    print(solution(ractangle, characterX, characterY, itemX, itemY))

    ractangle = [[2,2,5,5],[1,3,6,4],[3,1,4,6]]
    characterX = 1
    characterY = 4
    itemX = 6
    itemY = 3
    print(solution(ractangle, characterX, characterY, itemX, itemY))