def checkSeq(num: int):
    num_str = str(num)
    if len(num_str) == 1:
        return True

    else:
        diff = int(num_str[1]) - int(num_str[0])
        for i_ns in range(1, len(num_str)):
            _diff = int(num_str[i_ns]) - int(num_str[i_ns-1])
            if diff == _diff:
                continue
            else:
                return False
        return True

n = int(input())
cnt = 0
for _n in range(1, n+1):
    if checkSeq(_n):
        cnt += 1
print(cnt)