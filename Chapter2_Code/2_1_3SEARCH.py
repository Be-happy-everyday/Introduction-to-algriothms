from asyncio.windows_events import NULL



def SEARCH(A,v):
    for j in range(len(A)):
        if v == A[j]:
            return j
    return f"This number {v} doesn't exit!"

print(SEARCH([1,2,3,4,5,6,7,8,9], 23))