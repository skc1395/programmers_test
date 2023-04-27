import math

def solution(n):
    num = 0
    for i in range(1,n+1):
        if math.factorial(i) <= n:
            num = i
        else:
            break
    return num
            