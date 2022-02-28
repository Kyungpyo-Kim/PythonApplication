ops = {
    "@": lambda x: x * 3,
    "%": lambda x: x + 5,
    "#": lambda x: x-7,
}

test_case = int(input())

for i in range(test_case):
    data = input().split()
    x = float(data[0])
    for op in data[1:]:
        x = ops.get(op)(x)
    print(f"{x:.02f}")