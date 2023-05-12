def solution(score):
    count = 1
    answer = []
    for i in range(0,len(score)):
        for j in range(0,len(score)):
            if sum(score[i]) < sum(score[j]):
                count += 1
        answer.append(count)
        count = 1
    return answer