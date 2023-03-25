# https://school.programmers.co.kr/learn/courses/30/lessons/161989

def solution(n, m, section):
    answer = 0
    x = section[0]
    for v in section:
        if x <= v:
            x = (v + m)
            answer += 1

    return answer
