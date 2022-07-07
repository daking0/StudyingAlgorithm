#https://school.programmers.co.kr/learn/courses/30/lessons/12931
def solution(n):
    answer = 0
    for i in list(str(n)):
        answer += int(i)
    return answer
    
    # 다른사람 참고 코드
    # return sum(map(int,str(n)))
