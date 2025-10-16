class Solution(object):
    def findSmallestInteger(self, nums, value):
        """
        :type nums: List[int]
        :type value: int
        :rtype: int
        """
        rem = [0] * value
        for i in nums:
            r = i % value
            rem[r] += 1
        i=0
        while rem[i%value]:
            rem[i%value]-=1
            i+=1
        return i
        
nums = [1,-10,7,13,6,8] 
value = 5
print(Solution().findSmallestInteger(nums, value))