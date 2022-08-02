#https://school.programmers.co.kr/learn/courses/30/lessons/12926
def solution(s, n):
    answer = ''
    tempnum = 0 
    for i in s:
        tempnum = ord(i)
        if(tempnum == 32): 
            answer += chr(tempnum)
        else:
            if(tempnum in range(65,91)):
                tempnum += n
                if(tempnum > 90):
                    tempnum -= 26
                    answer += chr(tempnum)
                else:
                    answer += chr(tempnum)
            elif(tempnum in range(97,123)):
                tempnum += n
                if(tempnum > 122):
                    tempnum -= 26
                    answer += chr(tempnum)
                else:
                    answer += chr(tempnum)  
            
    return answer
