"""
max_slice_sum.py
"""


def solution(array: list) -> int:
    """solution
    get maximum summation of slices

    Args:
        array (list): array

    Returns:
        int: maximum summation
    """
    acc_sum = [0]
    len_array = len(array)
    for idx in range(len_array):
        acc_sum.append(acc_sum[-1] + array[idx])

    right_max_list = [0 for _ in range(len(acc_sum))]
    right_max_list[-1] = acc_sum[-1]
    right_max = acc_sum[-1]
    for idx in reversed(range(len(acc_sum) - 1)):
        right_max = max(right_max, acc_sum[idx])
        right_max_list[idx] = right_max

    max_sum = array[0]
    left_sum = 0
    for idx in range(len_array):
        left_sum = min(left_sum, acc_sum[idx])
        summation = right_max_list[idx + 1] - left_sum
        max_sum = max(max_sum, summation)

    return max_sum


if __name__ == "__main__":
    print(solution([3, 2, -6, 4, 0]))
    print(solution([-10]))
    print(solution([-10, -10]))
