# 로또의 최고 순위와 최저 순위
# https://school.programmers.co.kr/learn/courses/30/lessons/77484

def solution(lottos, win_nums):
    min_a = [r for r in lottos if r in win_nums]
    unknown_a = [r for r in lottos if r == 0]

    x = 7 - (len(min_a) + len(unknown_a))
    y = 7 - len(min_a)
    
    if len(unknown_a) == 6:
        x = 1
        y = 6
    elif len(unknown_a) == 0 and len(min_a) == 0:
        x = 6
        y = 6
    
    return [x, y]
