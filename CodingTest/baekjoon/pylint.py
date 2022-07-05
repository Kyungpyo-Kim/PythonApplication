"""_summary_
"""

def solution(A: list) -> int:
    """
    solution

    args:
        A(list): array, within the range [0..100,000]
                 each element of array  is an integer
                 within the range [-2,147,483,648..2,147,483,647]

    return:
        int: number of inversions
             -1 if number of inversions is larger than large_num

    """
    large_num = 1000000000
    inversion = 0
    sorted_arr = sorted(range(len(A)), key=lambda x: A[x])
    for idx, origin in enumerate(sorted_arr):
        if idx > origin:
            inversion += idx - origin
            if inversion > large_num:
                return -1

    return inversion
