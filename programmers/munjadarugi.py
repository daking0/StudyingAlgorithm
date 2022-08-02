#https://school.programmers.co.kr/learn/courses/30/lessons/12918
def solution(s):
    answer = True
    if((len(s)==4 or len(s)==6) and s.isdigit()):
        return answer
    else:
        answer = False
    return answer
