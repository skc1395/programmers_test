def solution(num, k):
    list_num = []
    for i in str(num):
        list_num.append(i)
    try:
        return list_num.index(str(k))+1
    except ValueError:
        return -1