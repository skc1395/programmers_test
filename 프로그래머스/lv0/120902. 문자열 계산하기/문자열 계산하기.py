def solution(my_string):
    my_string = my_string.split()
    sol = int(my_string[0])
    for i in range(0, len(my_string)):
        if my_string[i] == '+':
            sol += int(my_string[i+1])
        elif my_string[i] == '-':
            sol -= int(my_string[i+1])
    return sol