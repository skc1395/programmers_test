def solution(my_str, n):
    array = []
    index_num = 0
    for i in range(0,len(my_str)//n):
        array.append(my_str[index_num:index_num+n])
        index_num += n
    if (len(my_str)%n) != 0:
        array.append(my_str[index_num:])
    return array