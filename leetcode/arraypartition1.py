#sort로 정렬 후, 앞에서부터 2개씩 작은 수 찾아서 더해주기
class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        total = 0
        i = 0
        while i < len(nums)-1:
            total += min(nums[i],nums[i+1])
            i += 2
        return total
        
#sort로 정렬 후, 짝수번째가 작은 숫자이므로 바로 짝수번째 수만 더하기

class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        total = 0
        for i, num in enumerate(nums):
            if (i%2 ==0):
                total += num
        return total

# 더 간단한 코드 : sort한 list를 2개씩 짝수번째 위치만 sum
class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        return sum(sorted(nums)[::2])
# 출처: https://diking.tistory.com/58?category=554860 [Digking's cave:티스토리]
