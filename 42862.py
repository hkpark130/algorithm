# 체육복
# https://school.programmers.co.kr/learn/courses/30/lessons/42862

def binary_search(target, sorted_data): # 정렬된 배열을 기반
    start = 0
    end = len(sorted_data) - 1

    while start <= end:
        mid = (start + end) // 2

        if sorted_data[mid] == target:  # 값 찾음
            return mid
        elif sorted_data[mid] < target: # 기준값 보다 오른쪽
            start = mid + 1
        else:                           # 기준값 보다 왼쪽
            end = mid -1
    
    return None

def find_reserve(val, lost, reserve):
    found = True
    if(binary_search(val, reserve) is not None):
        reserve.remove(val)
    elif(binary_search(val-1, reserve) is not None and binary_search(val-1, lost) is None):
        reserve.remove(val-1)
    elif(binary_search(val+1, reserve) is not None and binary_search(val+1, lost) is None):
        reserve.remove(val+1)
    else:
        found = False

    return found

def solution(n, lost, reserve):
    lost.sort()
    reserve.sort()
    cnt_lost = len(lost)
    for val in lost:
        if( find_reserve(val, lost, reserve) ):
            cnt_lost = cnt_lost - 1

    return n - cnt_lost
