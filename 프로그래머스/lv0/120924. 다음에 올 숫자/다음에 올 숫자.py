def solution(common):
    #등차수열일 경우
    if common[1] * 2 == common[0] + common[2]:
        return common[-1] + common[1] - common[0]
    #등비수열일 경우
    elif common[1] ** 2 == common[0] * common[2]:
        return common[-1] * (common[1] / common[0])