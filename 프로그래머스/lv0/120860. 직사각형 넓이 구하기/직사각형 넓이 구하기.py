def solution(dots):
    width = 0
    length = 0
    if dots[0][0] != dots[1][0]:
        width = abs(dots[0][0]-dots[1][0])   
    if dots[0][0] != dots[2][0]:
        width = abs(dots[0][0]-dots[2][0])
    if dots[0][1] != dots[1][1]:
        length = abs(dots[0][1]-dots[1][1])
    if dots[0][1] != dots[2][1]:
        length = abs(dots[0][1]-dots[2][1])
    return width*length