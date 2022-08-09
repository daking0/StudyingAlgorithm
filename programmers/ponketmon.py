#https://school.programmers.co.kr/learn/courses/30/lessons/1845
# set으로 중복제거 후 개수만 확인
def solution(nums):
    answer = 0
    templist = list(set(nums))
    if(len(templist) > (len(nums)/2)):
        return len(nums) /2
    else:
        return len(templist)
    return answer

# 하나씩 확인하는 방법
def solution(nums):
    answer = 0
    templist = []
    for i in nums:
        if i not in templist:
            templist.append(i)
    if(len(templist) > (len(nums)/2)):
        return len(nums) /2
    else:
        return len(templist)
    return answer
출처: https://diking.tistory.com/69?category=554860 [Digking's cave:티스토리]
