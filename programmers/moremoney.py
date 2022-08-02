# https://school.programmers.co.kr/learn/courses/30/lessons/82612
def solution(price, money, count):
    answer = 0
    while(count>0):
        money -= (price*count)
        count -=1
    if(money<0):
        return abs(money)
    elif(money>0):
        return 0
    return answer
