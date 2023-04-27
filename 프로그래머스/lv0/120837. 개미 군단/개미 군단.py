def solution(hp):
    count = (hp//5) + ((hp%5)//3) + ((hp%5)%3)
    return count