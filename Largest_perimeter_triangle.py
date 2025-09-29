class Solution(object):
    def largestPerimeter(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort(reverse=True)
        for i in range(len(nums)-2):
            c, b, a = nums[i], nums[i+1], nums[i+2]
            if c < b + a:
                return a+b+c

        
nums = [3,6,2,3]
print(Solution().largestPerimeter(nums))