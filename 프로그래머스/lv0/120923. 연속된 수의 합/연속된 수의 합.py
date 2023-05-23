def solution(num, total):
    answer = []
    avg = int(total/num)
    num//2
    #num이 홀수
    if num % 2 == 1:
        for i in range(-(num//2), (num//2)+1):
            answer.append(avg + i)
    #num이 짝수
    else:
        for i in range(-(num//2)+1, (num//2)+1):
            answer.append(avg + i)
    return answer