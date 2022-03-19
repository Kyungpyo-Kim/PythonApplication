test_case = int(input())
for _ in range(test_case):
    cnt = 1
    score = 0
    result = input()
    for r in result:
        if r == "O":
            score += cnt
            cnt += 1
        else:
            cnt = 1
    print(score)