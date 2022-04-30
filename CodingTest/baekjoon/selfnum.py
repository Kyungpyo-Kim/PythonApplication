max_num = 10000
no_self_num = [False for _ in range(max_num)]

def seq(num):
    return sum(list(map(int, str(num)))) + num

for i in range(1, max_num):
    if no_self_num[i-1]:
        continue
    else:
        num = i
        while True:
            num = seq(num)
            if num >= max_num:
                break
            else:
                no_self_num[num-1] = True

for i in range(1, max_num):
    if not no_self_num[i-1]:
        print(i)