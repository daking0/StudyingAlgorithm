# https://school.programmers.co.kr/learn/courses/30/lessons/68644
def solution(numbers):
    answer = []
    for i in range(len(numbers)):
        for r in range(i+1,len(numbers)):
            answer.append(numbers[i]+numbers[r])
    anserset = set(answer)
    answer = list(anserset)
    answer.sort()
    return answer
