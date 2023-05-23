def solution(A, B):
    count = 0
    if A == B:
        return 0
    for i in range(0,len(A)):
        count += 1
        A = A[-1]+A[0:-1]
        if A == B:
            return count
    return -1