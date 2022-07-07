# https://programmers.co.kr/learn/courses/30/lessons/12935

def solution(arr):
    answer = []
    arr.remove(min(arr))
    if(len(arr) == 0):
        answer = [-1]
    else:
        answer = arr
    return answer
