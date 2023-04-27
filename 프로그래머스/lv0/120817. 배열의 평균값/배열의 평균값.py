import math

def solution(numbers):
    Sum = 0
    Avg = 0
    for i in numbers:
        Sum += i
    Avg = Sum / len(numbers)
    if Avg - int(Avg) == 0 or Avg - int(Avg) == 0.5:
        return Avg
    else: return round(Avg)
    
    # answer = 0
    # return answer