def solution(n):
    sol = []
    for i in range(1,n+1):
        if n % i == 0:
            sol.append(i)
    return sol