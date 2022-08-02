# https://school.programmers.co.kr/learn/courses/30/lessons/42840?language=python3 
def solution(answers):
    answer = []
    num1 = [1,2,3,4,5]
    num2 = [2,1,2,3,2,4,2,5]
    num3 = [3,3,1,1,2,2,4,4,5,5]
    result=[0,0,0]
    for i in range(0,len(answers)):
        if(answers[i]==num1[i%5]): result[0] +=1
        if(answers[i]==num2[i%8]): result[1] +=1
        if(answers[i]==num3[i%10]): result[2] +=1  
    
    maxnum = max(result)
    for i in range(0,3):
        if(result[i] == maxnum): answer.append(i+1)
    
    return answer
