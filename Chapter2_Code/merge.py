from asyncio.windows_events import NULL
from cmath import inf
from math import floor


def merge(A,p,q,r):
    n1 = q - p + 1
    n2 = r - q
    # Let L[1..(n1 + 1)] and R[1.. (n2 + 1)] be new arrays.
    L = [0 for i in range(n1+1)]
    R = [0 for i in range(n2+1)]

    for i in range(n1+1):
        L[i] = A[p + i]
    L[-1] = inf

    for i in range(n2 + 1):
        if i != n2:
            R[i] = A[q + i + 1]
        else:
            R[i] = inf

    i, j = 0, 0
    A = []

    for k in range(r - p + 1):
        if L[i] < R[j]:
            A.append(L[i])
            i = i + 1
        else:
            A.append(R[j])
            j = j + 1

    return A


def merge_sort(A, p=0, r=-1):
    if p < r:
        q = int((p + r) / 2)
        merge_sort(A, p, q)
        merge_sort(A, q+1, r)
        A[p:r+1] = merge(A, p, q, r)

        return A
