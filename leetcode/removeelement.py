# https://leetcode.com/explore/learn/card/array-and-string/205/array-two-pointer-technique/1151/
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        latnum = 0
        for i in range(0,len(nums)):
            if(nums[i] != val):
                nums[latnum] = nums[i]
                latnum += 1
                
        return latnum
같은 경우에 pop으로 빼면서 했더니 n
