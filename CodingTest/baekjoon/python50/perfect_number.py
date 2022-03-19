while True:
    n = int(input())
    if n == -1:
        break
    else:
        factors = [1]
        # O(N^(1/2))
        for i in range(2, int(n**0.5)+1):
            if n % i == 0:
                factors.extend([i, n//i])
        if sum(factors) == n:
            print(f"{n} = ", end='')
            for f in factors:
                print(f"{f}", end='')
                if f != factors[-1]:
                    print(" + ", end='')
                else:
                    print()
        else:
            print(f"{n} is NOT perfect.")