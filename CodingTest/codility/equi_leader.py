def solution(A):
    right = dict()
    for elem in A:
        right[elem] = right.get(elem, 0) + 1

    cnt = 0
    left = dict()
    len_A = len(A)
    left_lead_max = -1
    left_lead = -1

    for idx in range(len_A-1):
        left[A[idx]] = left.get(A[idx], 0) + 1
        right[A[idx]] -= 1
        
        if left[A[idx]] > left_lead_max:
            left_lead_max = left[A[idx]]
            left_lead = A[idx]
        
        if left[left_lead] > (idx+1)//2 and right[left_lead] > (len_A - 1 - idx)//2:
            cnt += 1

    return cnt

print(solution([4,3,4,4,4,2]))