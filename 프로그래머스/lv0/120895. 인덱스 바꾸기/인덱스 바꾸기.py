def solution(my_string, num1, num2):
    sol = ""
    for i in range(0,len(my_string)):
        if i != num1 and i != num2:
            sol += my_string[i]
        elif i == num1:
            sol += my_string[num2]
        elif i == num2:
            sol += my_string[num1]
    return sol