def solution(s):
    answer = []
    count = 0
    for i in s:
        for j in s:
            if i == j:
                count += 1
        if count == 1:
            answer.append(i)
        count = 0
    answer.sort()
    sol = ''.join(s for s in answer)
    return sol