# https://programmers.co.kr/learn/courses/30/lessons/12944

def solution(arr):
    answer = 0
    for i in arr:
        answer += i
    answer = answer/len(arr)
    return answer
