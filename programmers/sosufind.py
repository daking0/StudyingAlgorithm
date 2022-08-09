#https://school.programmers.co.kr/learn/courses/30/lessons/12921
def solution(n):
    num=set(range(2,n+1)) # 1과 n을 제외한 전체 집합

    for i in range(2,n+1): 
        if i in num: # 만약 i가 num 집합에 있다면
            num-=set(range(2*i,n+1,i)) # set으로 해당 수의 배수들을 리스트화해서 삭제
    return len(num) # 남아있는 소수의 개수 리턴
출처: https://diking.tistory.com/74?category=554860 [Digking's cave:티스토리]
