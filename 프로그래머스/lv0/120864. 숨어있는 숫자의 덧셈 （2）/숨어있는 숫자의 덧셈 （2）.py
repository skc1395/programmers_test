def solution(my_string):
    num_list = []
    temp = ''
    for i in my_string:
        if i.isdigit():
            temp += i
        else:
            if temp != '':
                num_list.append(temp)
                temp = ''
    if temp != '':
        num_list.append(temp)
        temp = ''
    return sum(int(i) for i in num_list)