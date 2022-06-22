# https://programmers.co.kr/learn/courses/30/lessons/12947
def solution(x):
    answer = True
    tempnum = 0
    strnum = str(x)
    for i in range(0,len(strnum)):
        tempnum += int(strnum[i])
    if(x%tempnum == 0):
        answer = True
    else:
        answer = False
    return answer
