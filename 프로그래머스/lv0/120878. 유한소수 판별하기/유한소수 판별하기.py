def solution(a, b):
    gcd = 0
    cd = []
    for i in range(1, min(a,b)+1):
        if (a%i==0) and (b%i==0):
            gcd = i
    for i in range(1,b//gcd + 1):
        if (b//gcd)%i == 0:
            cd.append(i)
    for i in cd[1:]:
        if (i%2!=0) and (i%5!=0):
            return 2
    return 1
    # if (b//gcd)
    #     return 1
    # else:
    #     return 