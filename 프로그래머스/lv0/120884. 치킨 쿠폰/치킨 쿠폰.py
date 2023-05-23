def solution(chicken):
    chicken_count = 0
    coupon_count = chicken
    while coupon_count >= 10:
        chicken_count += 1
        coupon_count -= 9
    return chicken_count