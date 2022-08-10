# https://school.programmers.co.kr/learn/courses/30/lessons/12977
from itertools import combinations;

def solution(nums):
    answer = 0
    for i in combinations(nums,3):
        temnum = sum(i)
        flag = True
        for i in range(2,temnum):
            if(temnum%i == 0):
                flag = False
                break
        if(flag):
            answer += 1

    return answer
