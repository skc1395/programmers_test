def solution(emergency):
    answer = []
    count = 0
    for i in emergency:
        for j in emergency:
            if i > j:
                count+=1
        answer.append(len(emergency) - count)
        count = 0
    return answer