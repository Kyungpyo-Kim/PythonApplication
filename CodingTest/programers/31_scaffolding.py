dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def solution(board, aloc, bloc):
    visited = [[False for _ in range(len(board[0]))] for _ in range(len(board))]

    def game(curx, cury, opx, opy):
        if visited[curx][cury]:
            return 0

        move = 0
        for i in range(4):
            nx = curx + dx[i]
            ny = cury + dy[i]
            if (
                0 <= nx < len(board)
                and 0 <= ny < len(board[0])
                and board[nx][ny] == 1
                and not visited[nx][ny]
            ):
                visited[curx][cury] = True
                new_move = game(opx, opy, nx, ny) + 1
                visited[curx][cury] = False  # backtracking
                
                # 현재 지고 있고, 다음 게임도 지는 경우
                if move % 2 == 0 and new_move % 2 == 0:
                    move = max(move, new_move)  # 최대한 많이 move
                # 현재 이기고 있고, 다음 게임도 이기는 경우
                elif move % 2 == 1 and new_move % 2 == 1:
                    move = min(move, new_move)  # 최대한 적게 move
                # 현재 지고 있고, 다음 게임 이기는 경우
                elif move % 2 == 0 and new_move % 2 == 1:
                    move = new_move

        return move

    return game(aloc[0], aloc[1], bloc[0], bloc[1])


if __name__ == "__main__":
    board = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
    aloc = [1, 0]
    bloc = [1, 2]
    print(solution(board, aloc, bloc), 5)
    # board = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
    # aloc = [1, 0]
    # bloc = [1, 2]
    # print(solution(board, aloc, bloc), 4)
    # board = [[1, 1, 1, 1, 1]]
    # aloc = [0, 0]
    # bloc = [0, 4]
    # print(solution(board, aloc, bloc), 4)
    # board = [[1]]
    # aloc = [0, 0]
    # bloc = [0, 0]
    # print(solution(board, aloc, bloc), 0)
