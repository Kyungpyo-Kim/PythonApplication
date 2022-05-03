# Combination

```python
def combination(arr, m):
    n = len(arr)
    if m == 0:
        return []

    comb = []
    for i in range(n):
        if m == 1:
            comb.append([arr[i]])
        else:
            sub_comb = combination(arr[i+1:], m-1)
            for sc in sub_comb:
                comb.append([arr[i]] + sc)
    return comb
```

```python
def permutation_with_repetition(arr, m):
    if m == 0:
        return []
    if m == 1:
        return [[a] for a in arr]
    
    res = list()
    n = len(arr)
    for i in range(n):
        sub_pr = permutation_with_repetition(arr, m-1)
        for spr in sub_pr:
            res.append([arr[i]] + spr)
            
    return res
```