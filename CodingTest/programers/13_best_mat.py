# 프로그래머스 레벨3 최적의행렬 연습문제

max_size = 200


def solution(matrix_sizes):
    table = [[0 for _ in range(max_size)] for _ in range(max_size)]

    def calculate(i, j):
        if i == j:
            return 0
        if table[i][j]:
            return table[i][j]
        if j - i == 1:
            table[i][j] = matrix_sizes[i][0] * matrix_sizes[i][1] * matrix_sizes[j][1]
            return table[i][j]

        min_value = 2**31
        for k in range(j - i):
            m = i + k
            value = (
                calculate(i, m)
                + calculate(m + 1, j)
                + matrix_sizes[i][0] * matrix_sizes[m][1] * matrix_sizes[j][1]
            )
            min_value = min(value, min_value)

        table[i][j] = min_value
        return table[i][j]

    return calculate(0, len(matrix_sizes) - 1)


if __name__ == "__main__":
    matrix_sizes = [[5, 3], [3, 10], [10, 6]]
    print(solution(matrix_sizes))
    matrix_sizes = [[5, 3], [3, 10], [10, 6], [6, 2]]
    print(solution(matrix_sizes))
