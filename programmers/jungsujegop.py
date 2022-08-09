#https://school.programmers.co.kr/learn/courses/30/lessons/12934
import math;

def solution(n):
    answer = 0
    tempnum = math.sqrt(n)
    if(tempnum.is_integer()):
        answer = math.pow((tempnum+1),2)
    else:
        return -1
    return answer
출처: https://diking.tistory.com/72?category=554860 [Digking's cave:티스토리]
