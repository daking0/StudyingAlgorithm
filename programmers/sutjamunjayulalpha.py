# https://school.programmers.co.kr/learn/courses/30/lessons/81301
def solution(s):
    answer = 0
    tempans = ""
    temp = ""
    diclist = {'zero':0,'one':1,'two':2,'three':3,'four':4,'five':5,'six':6,'seven':7,'eight':8,'nine':9}
    
    for i in s:
        if(i.isdigit()):
            tempans += i
        else:
            temp += i
        if temp in diclist.keys():
                tempans += str(diclist[temp])
                temp = ""
    answer = int(tempans)
    return answer
