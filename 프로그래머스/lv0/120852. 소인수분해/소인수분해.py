def solution(n):
    sol_list = []
    for i in range(2,n+1):
        if n % i == 0:
            for j in range(2,i+1):
                if i % j == 0 and j != i:
                    break
                if j == i:
                    sol_list.append(i)
    return sol_list
            
            