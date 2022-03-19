test_case = int(input())

results = {
    "Q1": 0,
    "Q2": 0,
    "Q3": 0,
    "Q4": 0,
    "AXIS": 0,
}

for _ in range(test_case):
    a, b = map(int, input().split())
    if a*b == 0:
        results["AXIS"] += 1
    elif a > 0 and b > 0:
        results["Q1"] += 1
    elif a < 0 and b > 0:
        results["Q2"] += 1
    elif a < 0 and b < 0:
        results["Q3"] += 1
    elif a > 0 and b < 0:
        results["Q4"] += 1
    else:
        pass

[print(f"{key}: {value}") for key, value in results.items()]