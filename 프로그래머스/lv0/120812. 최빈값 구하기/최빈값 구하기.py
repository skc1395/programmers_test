from collections import Counter

def solution(array):
    c = Counter(array)
    mode = c.most_common(1)
#요소가 모두 같은 숫자일때
    if len(array) == mode[0][1]:
        return mode[0][0]
#요소가 다른 숫자일때       
    mode = c.most_common(2)
    if mode[0][0] != mode[1][0] and mode[0][1] == mode[1][1]:
        return -1
    else:
        return mode[0][0]
