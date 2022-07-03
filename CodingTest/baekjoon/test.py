from bigO import BigO
from random import randint
import timeit

"""
----------------------- SOLUTION -----------------------------------------------
"""
def solution(A: list) -> int:
    """_summary_

    Args:
        A (list): _description_

    Returns:
        int: _description_
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

    _, inversion = merge_sort(A, 0)
    return inversion

"""
----------------------- BIG O -----------------------------------------------
https://github.com/pberkes/big_O
"""

def test(array):
    # for a in array:
    solution(array)
    return

lib = BigO()
# lib.runtime(test, "random", 10000)
# lib.runtime(test, "sorted", 10000)
lib.test(test, "random")
lib.test(test, "sorted")
lib.test(test, "reversed")
lib.test(test, "partial")
lib.test(test, "Ksorted")
