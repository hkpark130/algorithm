# https://school.programmers.co.kr/learn/courses/30/lessons/159994

def solution(cards1, cards2, goal):
    answer = 'Yes'
    for word in goal:
        if len(cards1) >0 and word == cards1[0]:
            cards1 = cards1[1:]
        elif len(cards2) >0 and word == cards2[0]:
            cards2 = cards2[1:]
        else:
            answer = 'No'
            break
    
    return answer
