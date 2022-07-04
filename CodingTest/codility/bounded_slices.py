def solution(A: list, K: int) -> str:
    """_summary_

    Args:
        A (list): _description_
        K (int): _description_

    Returns:
        str: _description_
    """
    length = len(A)
    max_val = [0 for _ in range(length+1)]
    min_val = [0 for _ in range(length+1)]
    max_pos = [0 for _ in range(length+1)]
    min_pos = [0 for _ in range(length+1)]

    max_head, max_tail = 0,0
    min_head, min_tail = 0,0

    max_val[0] = min_val[0] = A[0]

    result = 0
    end = 0
    for start in range(length):
        print(f"start: {start}")
        while end < length:
            print(start, end)
            print(max_val)
            print(max_pos)
            print(min_val)
            print(min_pos)

            while max_tail >= max_head and max_val[max_tail] <= A[end]:
                max_tail -= 1
            max_tail += 1
            max_val[max_tail] = A[end]
            max_pos[max_tail] = end

            while min_tail >= min_head and min_val[min_tail] >= A[end]:
                min_tail -= 1
            min_tail += 1
            min_val[min_tail] = A[end]
            min_pos[min_tail] = end

            if max_val[max_head] - min_val[min_head] <= K:
                end += 1
            else:
                break

        result += end - start

        if max_pos[max_head] == start:
            max_head += 1
        if min_pos[min_head] == start:
            min_head += 1

    return result

print(solution([3,5,7,6,3], 2))
