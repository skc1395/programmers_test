def solution(array):
    count = 0
    array_str = ''.join(str(i) for i in array)
    for i in range(0,len(array_str)):
        if array_str[i] == '7':
            count += 1
    return count