def solution(my_string):
    sol = ""
    str_list = sorted(list(my_string.lower()))
    for i in str_list:
        sol += i
    return sol