test_case = int(input())
cute = 0
for _ in range(test_case):
    cute += 1 if int(input()) else -1
if cute < 0:
    print("Junhee is not cute!")
else:
    print("Junhee is cute!")