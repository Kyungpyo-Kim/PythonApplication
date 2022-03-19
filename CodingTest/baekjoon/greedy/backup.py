n, k = map(int, input().split())
com = [int(input()) for _ in range(n)]

def permutation(arr, r):
    arr = sorted(arr)
    used = [False for _ in range(len(arr))]
    def choose(result, chosen, used):
        if len(chosen) == r:
            result.append(chosen[:])
            return
        else:
            for i, a in enumerate(arr):
                if not used[i]:
                    chosen.append(a)
                    used[i] = True
                    choose(result, chosen, used)
                    used[i] = False
                    chosen.pop()
        return
    
    result = list()
    choose(result, [], used)
    return result

def combination(arr, r):
    arr = sorted(arr)
    used = [False for _ in range(len(arr))]

    def generate(result, chosen):
        if len(chosen) == r:
            result.append(chosen[:])
            return

        start = arr.index(chosen[-1]) + 1 if chosen else 0
        for nxt in range(start, len(arr)):
            if (not used[nxt]) and (nxt==0 or arr[nxt-1] != arr[nxt] or used[nxt-1]):
                chosen.append(arr[nxt])
                used[nxt] = True
                generate(result, chosen)
                chosen.pop()
                used[nxt]=0
    result = []
    generate(result, [])
    return result

com_choosen = permutation(com, 2*k)
length_list = []

for i, cc in enumerate(com_choosen):
    combi = combination(cc, 2)
    for cmb in combi:
        length = abs(cmb[0]-cmb[1])
        res = [ c for c in cc if not c in cmb]
        length += abs(res[0] - res[1])
        length_list.append(length)

print(min(length_list))