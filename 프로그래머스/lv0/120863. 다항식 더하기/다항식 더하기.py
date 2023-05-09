def solution(polynomial):
    int_sum = 0
    x_sum = 0
    poly_list = polynomial.split(' ')
    for i in poly_list:
        if i[-1] == 'x':
            if i == 'x':
                x_sum += 1
            else:
                x_sum += int(i[0:-1])
        elif i != '+':
            int_sum += int(i)

    if x_sum == 0 or int_sum == 0:
        if x_sum == 0:
            return str(int_sum)
        else:
            if x_sum != 1:
                return "%dx" % x_sum
            else:
                return "x"
    else:
        if x_sum != 1:
            return "%dx + %d" % (x_sum, int_sum)
        else:
            return "x + %d" % int_sum
