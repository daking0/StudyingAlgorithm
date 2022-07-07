# https://school.programmers.co.kr/learn/courses/30/lessons/12933

def solution(n):
    answer = 0
    templist = []
    for i in str(n):
        templist.append(int(i))
    templist.sort(reverse=True)
    tempstring = ""
    for i in templist:
        tempstring = tempstring + str(i)
    answer = int(tempstring)
    return answer
    
    # 수정
def solution(n):
    answer = 0
    templist = list(str(n))
    templist.sort(reverse=True)
    
    answer = int("".join(templist))

    return answer
