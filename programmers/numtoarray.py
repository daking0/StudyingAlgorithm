# https://programmers.co.kr/learn/courses/30/lessons/12932
def solution(n):
    answer = []
    n = ''.join(reversed(str(n)))
    
    for i in n:
        answer.append(int(i))
    return answer
