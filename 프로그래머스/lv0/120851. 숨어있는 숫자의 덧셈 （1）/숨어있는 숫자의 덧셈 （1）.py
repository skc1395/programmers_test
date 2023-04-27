def solution(my_string):
    sum1 = 0
    for i in my_string:
        if i.isdigit():
            sum1 += int(i)
    return sum1