test_case = int(input())

for i in range(test_case):
    R, S = input().split()
    for s in S:
        print(s*int(R), end='')
    print()