import sys

input = sys.stdin.readline
# sudoku = [
#     [0, 3, 5, 4, 6, 9, 2, 7, 8],
#     [7, 8, 2, 1, 0, 5, 6, 0, 9],
#     [0, 6, 0, 2, 7, 8, 1, 3, 5],
#     [3, 2, 1, 0, 4, 6, 8, 9, 7],
#     [8, 0, 4, 9, 1, 3, 5, 0, 6],
#     [5, 9, 6, 8, 2, 0, 4, 1, 3],
#     [9, 1, 7, 6, 5, 2, 0, 8, 0],
#     [6, 0, 3, 7, 0, 1, 9, 5, 2],
#     [2, 5, 8, 3, 9, 4, 7, 6, 0],
# ]
# sudoku = [
#     [0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0],
# ]
sudoku = [list(map(int, input().split())) for _ in range(9)]
empty = []
for i in range(9):
    for j in range(9):
        if sudoku[i][j] == 0:
            empty.append([i,j])

def promising(i, j, k):
    # 1
    for l in range(9):
        if k == sudoku[i][l]:
            return False
    
    # 2
    for l in range(9):
        if k == sudoku[l][j]:
            return False
    
    # 3
    sub_i = i//3
    sub_j = j//3
    for si in range(sub_i*3, sub_i*3+3):
        for sj in range(sub_j*3, sub_j*3+3):
            if k == sudoku[si][sj]:
                return False

    return True

def fill(idx, find_solution):
    if find_solution:
        return find_solution
        
    if len(empty) == idx:
        find_solution = True
        for i in range(9):
            print(*sudoku[i])
        return find_solution

    for k in range(1, 10):
        i, j = empty[idx]
        if promising(i, j, k):
            sudoku[i][j]= k
            find_solution = fill(idx+1, find_solution)
            sudoku[i][j]= 0

    return find_solution

fill(0, False)