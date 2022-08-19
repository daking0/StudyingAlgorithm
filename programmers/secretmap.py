# https://school.programmers.co.kr/learn/courses/30/lessons/17681
def solution(n, arr1, arr2):
    answer = list(0 for i in range(0,n))
    
    temnew1 = list(0 for i in range(0,n))
    temnew2 = list(0 for i in range(0,n))
    # 2진수로 변경
    for i in range(0,n):
        temnew1[i] =format(arr1[i],'b')
        temnew2[i] =format(arr2[i],'b')
    
    # 자리수를 n자리로 맞추기
    for i in range(0,n):
        if(len(temnew1[i])<n):
            temnew1[i] = "0"*(n-len(temnew1[i])) + temnew1[i]
        if(len(temnew2[i])<n):
            temnew2[i] = "0"*(n-len(temnew2[i])) + temnew2[i]
    # 값 하나씩 + 한자리씩 비교
    for i in range(0,n):
        tem = ""
        #문자열을 list로 변경
        list1 = temnew1[i]
        list2 = temnew2[i]
        
        for r in range(0,n):
            if(list1[r]=="1" or list2[r]=="1"):
                tem += "#"                    
            elif(list1[r]=="0" and list2[r]=="0"):
                tem += " "
            else:
                tem += "#" 
        answer[i] = tem
        tem = ""    
    return answer
출처: https://diking.tistory.com/82 [Digking's cave:티스토리]
