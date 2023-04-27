def solution(numbers, direction):
    temp = 0
    if direction == "left":
        numbers.insert(len(numbers), numbers[0])
        numbers.remove(numbers[0])
    else:
        numbers.insert(0, numbers[len(numbers)-1])
        numbers.pop()
    return numbers