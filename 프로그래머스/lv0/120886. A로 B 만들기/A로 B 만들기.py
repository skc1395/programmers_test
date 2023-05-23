def solution(before, after):
    b_list = list(before)
    a_list = list(after)
    for i in b_list:
        try: 
            a_list.remove(i)
        except ValueError:
            continue    
    if a_list == []:
        return 1
    else:
        return 0