# 부족한 금액 계산하기
# https://school.programmers.co.kr/learn/courses/30/lessons/82612

def solution(price, money, count):
    sum_price = 0
    for i in range(1, count+1):
        sum_price = sum_price + price*i

    return sum_price - money if (sum_price > money) else 0
