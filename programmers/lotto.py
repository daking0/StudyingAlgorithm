# https://school.programmers.co.kr/learn/courses/30/lessons/77484
def solution(lottos, win_nums):
    minnum = 0 
    resultdic = {6:1,5:2,4:3,3:4,2:5,1:6,0:6} #로또 등수 dic
    
    #lottos 정렬 (0과 아닌 숫자 구분)
    lottos.sort()
    #0의 개수 확인 
    zeronum = lottos.count(0)
    
    #일치하는 개수 체크 
    for i in win_nums[::]:
        if i in lottos[zeronum:]:
            minnum +=1
     
    #최저값 = 정확히 일치하는 값
    #최고값 = 정확히 일치하는 값 + 알 수 없는 0이 전체 당첨일 경우
    
    return [resultdic[minnum + zeronum],resultdic[minnum]]
