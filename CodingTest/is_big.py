a, b = map(int, input().split())
while a + b:
    print("Yes") if a > b else print("No")
    a, b = map(int, input().split())