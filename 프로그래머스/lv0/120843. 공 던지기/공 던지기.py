def solution(numbers, k):
    num = (2*k-1) % len(numbers)
    if num == 0:
        return len(numbers)
    else:
        return num