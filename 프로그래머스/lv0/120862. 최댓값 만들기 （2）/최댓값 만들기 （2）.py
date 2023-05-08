def solution(numbers):
    Max = numbers[0]*numbers[1]
    for i in range(0,len(numbers)):
        for j in range(i+1,len(numbers)):
            if numbers[i]*numbers[j] > Max:
                Max = numbers[i]*numbers[j]
    return Max