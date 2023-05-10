def solution(board):
    count = 0
    n = len(board)
    if n == 1:
        if board[0][0] == 1:
            return count
        else:
            count +=1
            return count
    for i in range(0,n):
        for j in range(0,n):
            if board[i][j] == 1:
                if (1<=i<n-1) and (1<=j<n-1):
                    if board[i-1][j-1] != 1:
                        board[i-1][j-1] = 2
                    if board[i-1][j] != 1:
                        board[i-1][j] = 2
                    if board[i-1][j+1] != 1:
                        board[i-1][j+1] = 2                 
                    if board[i][j-1] != 1:
                        board[i][j-1] = 2
                    if board[i][j+1] != 1:
                        board[i][j+1] = 2                   
                    if board[i+1][j-1] != 1:
                        board[i+1][j-1] = 2  
                    if board[i+1][j+1] != 1:
                        board[i+1][j+1] = 2 
                    if board[i+1][j] != 1:
                        board[i+1][j] = 2        
                elif (i<1) and (1<=j<n-1):        
                    if board[i][j-1] != 1:
                        board[i][j-1] = 2
                    if board[i][j+1] != 1:
                        board[i][j+1] = 2                   
                    if board[i+1][j-1] != 1:
                        board[i+1][j-1] = 2  
                    if board[i+1][j+1] != 1:
                        board[i+1][j+1] = 2 
                    if board[i+1][j] != 1:
                        board[i+1][j] = 2                    
                elif n-1<=i and 1<=j<n-1:        
                    if board[i-1][j-1] != 1:
                        board[i-1][j-1] = 2
                    if board[i-1][j] != 1:
                        board[i-1][j] = 2
                    if board[i-1][j+1] != 1:
                        board[i-1][j+1] = 2                 
                    if board[i][j-1] != 1:
                        board[i][j-1] = 2
                    if board[i][j+1] != 1:
                        board[i][j+1] = 2                                      
                elif (1<=i<n-1) and (j<1):
                    if board[i-1][j] != 1:
                        board[i-1][j] = 2
                    if board[i-1][j+1] != 1:
                        board[i-1][j+1] = 2                 
                    if board[i][j+1] != 1:
                        board[i][j+1] = 2                   
                    if board[i+1][j+1] != 1:
                        board[i+1][j+1] = 2 
                    if board[i+1][j] != 1:
                        board[i+1][j] = 2
                elif (1<=i<n-1) and (n-1<=j):
                    if board[i-1][j-1] != 1:
                        board[i-1][j-1] = 2
                    if board[i-1][j] != 1:
                        board[i-1][j] = 2              
                    if board[i][j-1] != 1:
                        board[i][j-1] = 2                 
                    if board[i+1][j-1] != 1:
                        board[i+1][j-1] = 2  
                    if board[i+1][j] != 1:
                        board[i+1][j] = 2                   
                elif i<1 and j<1:            
                    if board[i][j+1] != 1:
                        board[i][j+1] = 2                   
                    if board[i+1][j+1] != 1:
                        board[i+1][j+1] = 2 
                    if board[i+1][j] != 1:
                        board[i+1][j] = 2                        
                elif i<1 and n-1<=j:           
                    if board[i][j-1] != 1:
                        board[i][j-1] = 2    
                    if board[i+1][j-1] != 1:
                        board[i+1][j-1] = 2  
                    if board[i+1][j] != 1:
                        board[i+1][j] = 2                                           
                elif n-1<=i and j<1:
                    if board[i-1][j] != 1:
                        board[i-1][j] = 2
                    if board[i-1][j+1] != 1:
                        board[i-1][j+1] = 2                 
                    if board[i][j+1] != 1:
                        board[i][j+1] = 2                   
                elif n-1<=i and n-1<=j:
                    if board[i-1][j-1] != 1:
                        board[i-1][j-1] = 2
                    if board[i-1][j] != 1:
                        board[i-1][j] = 2  
                    if board[i][j-1] != 1:
                        board[i][j-1] = 2                   
    for i in range(0,n):
        for j in range(0,n):
            if board[i][j] == 0:
                count += 1
    return count
            
