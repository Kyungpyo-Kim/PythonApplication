v = int(input())
vote = input()
a = b = 0
for i in range(v):
    a += (vote[i] == "A")
    b += (vote[i] == "B")
print("Tie") if a == b else print(["A", "B"][int(a<b)])