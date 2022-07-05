"""
merge_sort.py
"""

def solution(arr: list) -> int:
    """solution
    get the number of inversion (a, b) where a < b and arr[a] > arr[b]

    Args:
        arr (list): array

    Returns:
        int: return number of inversion
             return -1 if inversion is larger than 1000000000
    """
    def merge(left, right, inversion):
        if inversion == -1:
            return [], -1
        arr = []
        i = j = 0
        while i < len(left) or j < len(right):
            if j == len(right) or i != len(left) and left[i] <= right[j]:
                arr.append(left[i])
                i += 1
            else:
                arr.append(right[j])
                j += 1
                inversion += len(left) - i
                if inversion > 1000000000:
                    return [], -1
        return arr, inversion

    def merge_sort(arr, inversion):
        if len(arr) <= 1:
            return arr, inversion
        mid = len(arr) // 2
        left, inversion = merge_sort(arr[:mid], inversion)
        right, inversion = merge_sort(arr[mid:], inversion)
        return merge(left, right, inversion)

    _, inversion = merge_sort(arr, 0)
    return inversion
