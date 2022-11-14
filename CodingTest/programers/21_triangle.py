# 프로그래머스 레벨3 정수삼각형 동적계획법

def solution(triangle):
    table = [[0 for _ in range(len(triangle))] for _ in range(len(triangle))]
    table[0][0] = triangle[0][0]

    for i, tri in enumerate(triangle):
        for j, t in enumerate(tri):
            if i == 0 and j == 0:
                continue
            table[i][j] = table[i-1][j] + t
            if i-1 >= 0 and j-1 >= 0:
                table[i][j] = max(table[i][j], table[i-1][j-1] + t)

    return max(table[-1])

if __name__ == "__main__":
    triangle = [[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]
    print(solution(triangle))