
def CHOOSE(A,n):
    i = 0
    while i < n:
        min = A[i]
        index = i
        for j in range(i, n):
            if A[j] < A[i]:
                min = A[j]
                index = j
        A[index] = A[i]
        A[i] = min
        i += 1

    return A

print(CHOOSE([10,9,8,7,6,5,4,3,2,1,0],11))