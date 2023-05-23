def solution(i, j, k):
    count = 0
    for x in range(i,j+1):
        for j in range(0,len(str(x))):
            if str(k) == str(x)[j]:
                count += 1
    return count