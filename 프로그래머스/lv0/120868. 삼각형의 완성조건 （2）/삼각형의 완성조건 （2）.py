def solution(sides):
    count = 0
    # sides 배열에 가장 긴 변이 있는 경우
    x = max(sides[0],sides[1]) - min(sides[0],sides[1]) + 1
    while max(sides[0],sides[1]) < min(sides[0],sides[1]) + x and x < max(sides[0],sides[1]):
        x += 1
        count += 1
    
    # 배열 외에 가장 긴 변이 있는 경우
    y = max(sides[0],sides[1])
    while y < (sides[0]+sides[1]):
        y += 1
        count += 1
        
    return count