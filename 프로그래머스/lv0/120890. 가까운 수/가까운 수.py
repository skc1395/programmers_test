def solution(array, n):    
    temp = array[0]-n
    for i in array:
        if abs(i-n) < abs(temp):
            temp = i-n
        elif abs(i-n) == abs(temp) and i < temp+n:
            temp = i-n
    return array[array.index(temp+n)]