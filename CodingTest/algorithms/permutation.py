def recursive_permutation(arr, r):
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

def swap_permutation(arr, r):
    pool = tuple(arr)
    n = len(pool)

    indices = list(range(n))
    cycles = list(range(n, n-r, -1))
    pass

def generator_permutation(arr, r):
    for i in range(len(arr)):
        if r == 1:
            yield [arr[i]]
        else:
            for next in generator_permutation(arr[:i] + arr[i+1:], r-1):
                yield [arr[i]] + next

def itertools_permutation(arr, r):
    pool = tuple(arr)
    n = len(pool)
    indices = list(range(n))
    cycles = list(range(n, n-r, -1))
    print(indices)
    print(cycles)
    yield tuple(pool[i] for i in indices[:3])
    print("test")


print("resursion\n", recursive_permutation([1,2,3], 2))
print("generator\n", [i for i in generator_permutation([1,2,3], 2)])
print("itertools permutation\n",
[i for i in itertools_permutation([1,2,3], 3)]
)