def solution(n, numlist):
    sol = []
    for i in numlist:
        if i % n == 0:
            sol.append(i)
    return sol