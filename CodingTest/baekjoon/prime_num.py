def check_prime(num: int)->int:
    if num == 1:
        return 0
    if num == 2:
        return 1
    
    rt = int(num**0.5) + 1
    while rt > 1:
        if num % rt == 0:
            return 0
        else:
            rt -= 1
    return 1

input()
tot = 0
for n in map(int, input().split()):
    tot += check_prime(n)
print(tot)