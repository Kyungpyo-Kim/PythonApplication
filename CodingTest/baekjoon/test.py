import sys
input = sys.stdin.readline

letters = [list(input().strip()) for _ in range(5)]

result = []
for i in range(15):
    for j in range(5):
        if i < len(letters[j]):
            result.append(letters[j][i])
print("".join(result))