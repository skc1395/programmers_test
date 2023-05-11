def solution(lines):
    answer = []
    #0,1 비교
    if lines[0][0] <= lines[1][0]:
        if lines[1][0] < lines[0][1]:
            answer.append([lines[1][0],min(lines[0][1],lines[1][1])])
    else:
        if lines[0][0] < lines[1][1]:
            answer.append([lines[0][0],min(lines[0][1],lines[1][1])])
    #0,2 비교
    if lines[0][0] <= lines[2][0]:
        if lines[2][0] < lines[0][1]:
            answer.append([lines[2][0],min(lines[0][1],lines[2][1])])
    else:
        if lines[0][0] < lines[2][1]:
            answer.append([lines[0][0],min(lines[0][1],lines[2][1])])    
    #1,2 비교
    if lines[1][0] <= lines[2][0]:
        if lines[2][0] < lines[1][1]:
            answer.append([lines[2][0],min(lines[1][1],lines[2][1])])
    else:
        if lines[1][0] < lines[2][1]:
            answer.append([lines[1][0],min(lines[1][1],lines[2][1])])      
    #길이
    if len(answer) == 0:
        return 0
    elif len(answer) == 1:
        return (answer[0][1]-answer[0][0])
    elif len(answer) == 2:
        return ((answer[0][1]-answer[0][0]) + (answer[1][1]-answer[1][0]))
    else:
        return (max(answer[0][1],answer[1][1],answer[2][1]) - min(answer[0][0],answer[1][0],answer[2][0]))
