def solution(numlist, n):
    answer = [i-n for i in numlist]
    answer.sort()
    temp = 0
    for i in range(0,len(answer)):
        for j in range(i,len(answer)):
            if abs(answer[i]) > abs(answer[j]):
                temp = answer[j]
                answer[j] = answer[i]
                answer[i] = temp
            elif abs(answer[i]) == abs(answer[j]):
                if answer[i] < answer[j]:
                    temp = answer[j]
                    answer[j] = answer[i]
                    answer[i] = temp                    
            temp = 0
            
    for i in range(0,len(answer)):
        answer[i] += n
    return answer