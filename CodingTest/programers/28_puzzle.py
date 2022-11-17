# 프로그래머스 레벨3 퍼즐조각채우기 깊이너비우선탐색
from collections import deque
import copy


def solution(game_board, table):
    n = len(game_board)

    def bfs(table, x, y, num):
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        q = deque([[x, y]])
        ret = [[x, y]]
        visited = [[False for _ in range(n)] for _ in range(n)]
        visited[x][y] = True
        while q:
            cur = q.popleft()
            for dx, dy in directions:
                nx, ny = cur[0] + dx, cur[1] + dy
                if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                    if table[nx][ny] == num:
                        visited[nx][ny] = True
                        ret.append([nx, ny])
                        q.append([nx, ny])
        return ret

    def rotate(table):
        return [list(r) for r in zip(*table[::-1])]

    def normalize(empty):
        min_x, min_y = n, n
        for x, y in empty:
            min_x = min(min_x, x)
            min_y = min(min_y, y)
        for i in range(len(empty)):
            empty[i][0] -= min_x
            empty[i][1] -= min_y
        return empty

    def match(emptys, table):
        matched = 0
        for _ in range(4):
            table = rotate(table)
            for r in range(n):
                for c in range(n):
                    if table[r][c] == 1:
                        puzzle = bfs(table, r, c, 1)
                        puzzle_norm = normalize(copy.deepcopy(puzzle))
                        if puzzle_norm in emptys:
                            matched += len(puzzle)
                            table[r][c] = 2
                            for p in puzzle:
                                table[p[0]][p[1]] = 2
                            # remove matched empty
                            emptys.remove(puzzle_norm)
        return matched

    emptys = []
    for r in range(n):
        for c in range(n):
            if game_board[r][c] == 0:
                empty = bfs(game_board, r, c, 0)
                for e in empty:
                    game_board[e[0]][e[1]] = 2
                emptys.append(normalize(empty))

    matched = match(emptys, table)
    return matched


if __name__ == "__main__":
    game_board = [
        [1, 1, 0, 0, 1, 0],
        [0, 0, 1, 0, 1, 0],
        [0, 1, 1, 0, 0, 1],
        [1, 1, 0, 1, 1, 1],
        [1, 0, 0, 0, 1, 0],
        [0, 1, 1, 1, 0, 0],
    ]
    table = [
        [1, 0, 0, 1, 1, 0],
        [1, 0, 1, 0, 1, 0],
        [0, 1, 1, 0, 1, 1],
        [0, 0, 1, 0, 0, 0],
        [1, 1, 0, 1, 1, 0],
        [0, 1, 0, 0, 0, 0],
    ]
    print(solution(game_board, table))


def dfs(table, x, y, num):
    directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
    q = deque([[x, y]])
    ret = [[x, y]]
    visited = [[False for _ in range(n)] for _ in range(n)]
    visited[x][y] = True
    while q:
        cur = q.pop()
        for dx, dy in directions:
            nx, ny = cur[0] + dx, cur[1] + dy
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                if table[nx][ny] == num:
                    visited[nx][ny] = True
                    ret.append([nx, ny])
                    q.append([nx, ny])
    return ret


def dfs_recursion(table, x, y, num, visited):
    directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
    ret = [[x, y]]
    visited[x][y] = True
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
            if table[nx][ny] == num:
                ret += dfs_recursion(table, nx, ny, num, visited)
    return ret
