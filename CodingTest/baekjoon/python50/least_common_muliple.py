# test_case = int(input())

# for i in range(test_case):
#     a, b = map(int, input().split())
#     for j in range(max(a, b), a*b+1):
#         if j % a == 0 and j % b == 0:
#             print(j)
#             break

# Euclidean algorithm
def getGreatestCommonDivisor(a, b):
    while a:
        b, a = a, b % a
    return b

def getLeastCommonMultiple(a, b):
    return (a*b) // getGreatestCommonDivisor(a, b)

test_case = int(input())

for i in range(test_case):
    a, b = map(int, input().split())
    print(getLeastCommonMultiple(a, b))