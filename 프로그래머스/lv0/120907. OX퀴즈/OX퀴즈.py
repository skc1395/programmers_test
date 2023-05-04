def solution(quiz):
    temp = []
    sol = []
    for i in quiz:
        temp = i.split(" ")
        if temp[1] == "+":
            if (int(temp[0]) + int(temp[2])) == int(temp[4]):
                sol.append("O")
            else:
                sol.append("X")
        else:
            if (int(temp[0]) - int(temp[2])) == int(temp[4]):
                sol.append("O")
            else:
                sol.append("X")
    return sol