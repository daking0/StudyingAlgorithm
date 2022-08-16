# https://school.programmers.co.kr/learn/courses/30/lessons/12982
def solution(d, budget):
    answer = 0
    d.sort()
    totalnum = 0
    temn =0
    for i in d:
        totalnum += i
        if(totalnum <= budget):
            answer += 1
        else:
            break
    return answer
