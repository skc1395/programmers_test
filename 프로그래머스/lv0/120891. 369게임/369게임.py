def solution(order):
    sol = 0
    for i in range(6):
        if (order//(10**i))>=1 and (order//(10**i))%10 != 0 and ((order//(10**i))%10)%3==0:
            sol += 1
    return sol