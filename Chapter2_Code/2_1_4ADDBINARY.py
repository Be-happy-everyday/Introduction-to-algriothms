def BIADD(A,B,n):
    carrier = 0
    C = []
    for i in range(n):
        num_a = int(A[i])
        num_b = int(B[i])
        if num_a + num_b + carrier == 3:
            C.append(1)
            carrier = 1
        elif num_a + num_b + carrier == 2:
            C.append(0)
            carrier = 1
        elif num_a + num_b + carrier == 1:
            C.append(1)
            carrier = 0
        else:
            C.append(0)
            carrier = 0

    if carrier == 1:
        C.append(1)
    else:
        C.append(0)
    return C

print(BIADD('011','101',3))
