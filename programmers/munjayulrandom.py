# https://school.programmers.co.kr/learn/courses/30/lessons/12915
# sorted() 사용
def solution(strings, n):
    answer = []
    return sorted(strings, key=lambda x:(x[n],x))
    
# sort() 사용   
def solution(strings, n):
    answer = []
    strings.sort(key=lambda x:(x[n],x))
    answer = strings
    return answer
# 출처: https://diking.tistory.com/51?category=554860 [Digking's cave:티스토리]
