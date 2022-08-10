# https://school.programmers.co.kr/learn/courses/30/lessons/77884
def solution(left, right):
    answer = 0
    for i in range(left,right+1):
        temnum = 0
        #약수구하기
        for r in range(1,i+1):
            if(i%r ==0):
                temnum += 1
        if(temnum % 2 == 0):
            print
            answer += r
        else:
            answer -= r
    
    return answer
