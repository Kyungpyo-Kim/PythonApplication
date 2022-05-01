s = input()
ss = "".join([chr(a) for a in range(ord('a'), ord('z')+1)])
for i in ss:
    print(s.find(i), end=' ')