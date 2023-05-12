def solution(babbling):
    bablist = ["aya", "ye", "woo", "ma"]
    count = 0
    for i in babbling:
        for j in range(0, len(bablist)):
            i = i.replace(bablist[j]," ",1)
        i = i.replace(" ","")
        if i == "":
            count += 1
    return count
                      