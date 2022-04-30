# 정렬

## 선택 정렬
* 구현이 간단함
* N + N-1 + N-2 + ... + 2  -> O(N^2)
```python
array = [7 ,5, 9, 0, 3, 1, 6, 2, 4, 8]
for i in range(len(array)):
    min_idx = i
    for j in range(i+1, len(array)):
        if array[min_idx] > array[j]:
            min_idx = j
    array[i], array[min_idx] = array[min_idx], array[i]

print(array)
```

## 삽입 정렬
* 시간 복잡도는 O(N^2) 이지만, 거의 정렬되어 있는 상태에서는 빠르게 동작 (최소 O(N) 으로 동작)
```python
array = [7 ,5, 9, 0, 3, 1, 6, 2, 4, 8]
for i in range(1, len(array)):
    for j in range(i, 0, -1):
        if array[j] < array[j-1]:
            array[j-1], array[j] = array[j], array[j-1]
        else:
            break
print(array)
```

## 퀵 정렬
* 이상적인 경우 O(NlogN), 최악의 경우 O(N^2)


```python
array = [7 ,5, 9, 0, 3, 1, 6, 2, 4, 8]

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[0]
    tail = arr[1:]

    left_side = [x for x in tail if x <= pivot]
    right_side = [x for x in tail if x > pivot]

    return quick_sort(left_side) + [pivot] + quick_sort(right_side)

print(quick_sort(array))
```