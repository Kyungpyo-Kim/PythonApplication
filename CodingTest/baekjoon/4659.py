import sys

input = sys.stdin.readline

while True:
    password = input().strip()

    if password == "end":
        break

    flag1 = False
    for p in password:
        flag1 = flag1 or p in ["a", "e", "i", "o", "u"]

    flag2 = True
    cnt = 1
    prev = password[0] in ["a", "e", "i", "o", "u"]
    for p in password[1:]:
        p = p in ["a", "e", "i", "o", "u"]
        if p == prev:
            cnt += 1
            if cnt >= 3:
                flag2 = False
                break
        else:
            prev = p
            cnt = 1

    tmp = password.replace("ee", "")
    tmp = tmp.replace("oo", "")
    flag3 = True
    if tmp:
        cnt = 1
        prev = tmp[0]
        for p in tmp[1:]:
            if p == prev:
                cnt += 1
                if cnt >= 2:
                    flag3 = False
                    break
            else:
                prev = p
                cnt = 1

    flag = flag1 and flag2 and flag3
    print(f"<{password}> is{' ' if flag else ' not '}acceptable.")
