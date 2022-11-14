# 프로그래머스 레벨3 연습문제 2차원 동전 뒤집기

def solution(beginning, target):
    answer = 0
    dim_row = len(beginning)
    dim_col = len(beginning[0])

    answer = float("inf")

    for row in range(1 << dim_row):
        for col in range(1<<dim_col):
            matched = check(beginning, target, row, col)
            if matched:
                answer = min(answer, bin(row).count("1") + bin(col).count("1"))
    return answer if answer < float("inf") else -1

def check(beginning, target, row_mask, col_mask):
    dim_row = len(beginning)
    dim_col = len(beginning[0])
    for row in range(dim_row):
        r = 1 if row_mask & (1 << row) else 0
        for col in range(dim_col):
            c = 1 if col_mask & (1 << col) else 0
            if (beginning[row][col] + r + c) % 2 != target[row][col]:
                return False
    return True

if __name__ == "__main__":
    beginning = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]	
    target = [[1, 0, 1], [0, 0, 0], [0, 0, 0]]	
    print(solution(beginning, target))

    beginning = [[0, 1, 0, 0, 0], [1, 0, 1, 0, 1], [0, 1, 1, 1, 0], [1, 0, 1, 1, 0], [0, 1, 0, 1, 0]]
    target = [[0, 0, 0, 1, 1], [0, 0, 0, 0, 1], [0, 0, 1, 0, 1], [0, 0, 0, 1, 0], [0, 0, 0, 0, 1]]	
    print(solution(beginning, target))