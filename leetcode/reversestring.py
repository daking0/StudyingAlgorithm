# https://leetcode.com/explore/learn/card/array-and-string/205/array-two-pointer-technique/1183/
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        leftnum, rightnum = 0 , len(s)-1
        
        while (leftnum < rightnum ):
            s[leftnum],s[rightnum] = s[rightnum],s[leftnum]
            leftnum += 1
            rightnum -= 1
            
            
            
# 추가 풀이
class Solution:
    def reverseString(self, s: List[str]) -> None:
        s.reverse()
