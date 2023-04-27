def solution(s):
    list0 = []
    sum0 = 0
    list0 = s.split(' ')
    for i in range(0,len(list0)):
        if list0[i] == 'Z':
            sum0 -= int(list0[i-1])
        else:
            sum0 += int(list0[i])
    return sum0