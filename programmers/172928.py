# https://school.programmers.co.kr/learn/courses/30/lessons/172928

def solution(park, routes):
    answer = []
    w = len(park[0])
    h = len(park)
    for r in range(0,len(park)):
        if "S" in park[r]:
            x, y = park[r].index("S"), r
            break

    for r in range(0,len(routes)):
        d,n = routes[r].split(' ')
        tmp = [x,y]
        for i in range(1,int(n)+1):
            if d == 'E' and x+1 < w and park[y][x+1] != "X":
                x += 1
            elif d == 'W' and x-1 >= 0 and park[y][x-1] != "X":
                x -= 1
            elif d == 'S' and y+1 < h and park[y+1][x] != "X":
                y += 1
            elif d == 'N' and y-1 >= 0 and park[y-1][x] != "X":
                y -= 1
            else:
                x,y = tmp
                break
    answer = [y,x]
    return answer
