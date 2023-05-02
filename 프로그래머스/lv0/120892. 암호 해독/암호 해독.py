def solution(cipher, code):
    answer = ''
    for i in range(code,len(cipher),code):
        answer += cipher[i-1]
    if len(cipher) % code == 0:
        answer += cipher[len(cipher)-1]
    return answer