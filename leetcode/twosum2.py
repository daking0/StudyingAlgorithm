class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:        
        leftnum , rightnum = 0, len(numbers)-1
        
        while leftnum < rightnum :
            if(numbers[leftnum] + numbers[rightnum] == target):
                return [leftnum+1,rightnum+1]
            elif(numbers[leftnum] + numbers[rightnum] < target):
                leftnum += 1
            elif(numbers[leftnum] + numbers[rightnum] > target):
                rightnum -= 1
                
# sort 된 상태니까 값을 비교하면서, target보다 작으면 왼쪽을 크면 오른쪽을 하나씩 움직인다
# 출처: https://diking.tistory.com/59?category=554860 [Digking's cave:티스토리]
