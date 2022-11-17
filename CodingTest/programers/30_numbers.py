import sys
sys.setrecursionlimit(1000000)

weight = [
    [1,7,6,7,5,4,5,3,2,3],
    [7,1,2,4,2,3,5,4,5,6],
    [6,2,1,2,3,2,3,5,4,5],
    [7,4,2,1,5,3,2,6,5,4],
    [5,2,3,5,1,2,4,2,3,5],
    [4,3,2,3,2,1,2,3,2,3],
    [5,5,3,2,4,2,1,5,3,2],
    [3,4,5,6,2,3,5,1,2,4],
    [2,5,4,5,3,2,3,2,1,2],
    [3,6,5,4,5,3,2,4,2,1]
]

def solution(numbers):
    dp = {}
    length = len(numbers)
    def dfs(i, left, right):
        if i == length:
            return 0
        if (i, left, right) in dp:
            return dp[(i, left, right)]

        number = int(numbers[i])

        if left == number:
            dp[(i, left, right)] = 1 + dfs(i + 1, left, right)
            return dp[(i, left, right)]
        if right == number:
            dp[(i, left, right)] = 1 + dfs(i + 1, left, right)
            return dp[(i, left, right)]

        dp[(i, left, right)] = min(
            weight[right][number] + dfs(i + 1, left, number),
            weight[left][number] + dfs(i + 1, number, right),
        )
        return dp[(i, left, right)]

    return dfs(0, 4, 6)


if __name__ == "__main__":
    print(solution("1756"))
    print(solution("5123"))
