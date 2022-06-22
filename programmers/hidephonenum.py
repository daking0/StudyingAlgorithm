# https://programmers.co.kr/learn/courses/30/lessons/12948
def solution(phone_number):
    answer = ''
    templen = len(phone_number)
    answer = ('*'*(templen-4)) + phone_number[templen-4:]
    return answer
