def solution(my_string):
    sol = ""
    for i in my_string:
        if i.isupper():
            sol += i.lower()
        elif i.islower():
            sol += i.upper()
    return sol
