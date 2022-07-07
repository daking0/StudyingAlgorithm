# https://programmers.co.kr/learn/courses/30/lessons/12943
def solution(num):
    answer = 0
    
    while(True):
        if(num == 1):
            break
        if(answer == 500):
            break
        if(num % 2 == 0 ): 
            num = num//2
            answer += 1
        else:
            num = (num*3)+1
            answer += 1
    
    if(answer == 500):
        answer = -1
    
    return answer

