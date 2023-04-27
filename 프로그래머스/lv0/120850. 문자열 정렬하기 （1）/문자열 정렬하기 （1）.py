import re

def solution(my_string):
    str_list = list(my_string)
    num_list = []
    for i in str_list:
        if i == '0' or i =='1' or i =='2' or i =='3' or i =='4' or i =='5' or i =='6' or i =='7' or i =='8' or i =='9':
            num_list.append(int(i))
    num_list.sort()
    return num_list