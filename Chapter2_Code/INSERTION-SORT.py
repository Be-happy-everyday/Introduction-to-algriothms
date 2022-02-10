def INSERTION_SORT(A):

    for j in range(1,len(A)):
        key = A[j]
        #Insert A[j] into the sorted sequence A[1..j-1]
        i = j-1
        while i >= 0 and A[i] > key:
            A[i+1] = A[i]
            i -= 1
        A[i+1] = key
    
    return A

#print(INSERTION_SORT([10,9,8,7,6,5,4,3,2,1,0]))