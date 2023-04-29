def solution(my_string):
    solution = ""
    for i in range(0,len(my_string)):
        if my_string.find(my_string[i]) == i:
            solution += my_string[i]
    return solution