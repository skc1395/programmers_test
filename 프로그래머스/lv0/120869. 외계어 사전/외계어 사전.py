def solution(spell, dic):
    spell.sort()
    temp = []
    for i in dic:
        for j in i:
            temp.append(j)
        temp.sort()
        if spell == temp:
            return 1
        else:
            temp = []
    return 2