def solution(num_list, n):
    app_list = []
    answer = []
    num1 = 0
    loop = len(num_list) // n
    for i in range(0, loop):
        for j in range(0, n):
            app_list.append(num_list[num1])
            num1 += 1
        answer.append(app_list)
        app_list = []
    return answer