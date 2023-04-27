def solution(n):
    count = 0
    for i in range(1,n+1):
        check_num = 0
        for j in range(1,i+1):
            if i % j == 0:
                check_num += 1
        if check_num >= 3:
            count += 1
    return count