def combinations_itertools(iterable, r):
    pool = tuple(iterable)
    n = len(pool)
    if r > n:
        return
    indices = list(range(r))
    yield tuple(pool[i] for i in indices)
    while True:
        for i in reversed(range(r)):
            if indices[i] != i + n - r:
                break
        else:
            return
        indices[i] += 1
        for j in range(i + 1, r):
            indices[j] = indices[j - 1] + 1
        yield tuple(pool[i] for i in indices)

def combinations_recursion(iterable, r):
    n = len(iterable)
    for i in range(n):
        if r == 1:
            yield [iterable[i]]
        else:
            for next in combinations_recursion(iterable[i+1:], r-1):
                yield [iterable[i]] + next

print("combinations_itertools")
print(list(combinations_itertools(["a", "b", "c", "d"],3)))
print("combinations_recursion")
print(list(combinations_recursion(["a", "b", "c", "d"],3)))