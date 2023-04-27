def solution(age):
    answer = ""
    ary_s = "abcdefghij"
    ary_i = str(age)
    for i in range(len(ary_i)):
        answer += ary_s[int(ary_i[i])]
    return answer