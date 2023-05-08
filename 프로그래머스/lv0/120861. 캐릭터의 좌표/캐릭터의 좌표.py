def solution(keyinput, board):
    input_arry = [0,0]
    for i in keyinput:
        if i == 'up':
            if input_arry[1] < board[1]//2:
                input_arry[1] += 1
        elif i == 'down':
            if input_arry[1] > (-1)*(board[1]//2):
                input_arry[1] -= 1
        elif i == 'left':
            if input_arry[0] > (-1)*(board[0]//2):
                input_arry[0] -= 1
        elif i == 'right':
            if input_arry[0] < board[0]//2:
                input_arry[0] += 1

    
    return input_arry