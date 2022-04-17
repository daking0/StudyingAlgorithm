# https://programmers.co.kr/learn/courses/30/lessons/76501
def solution(absolutes, signs):
    answer = 0
    lennum = len(absolutes)

    for i in range(0, lennum):
        if (signs[i]):
            answer = answer + absolutes[i]
        else:
            answer = answer - absolutes[i]

    return answer