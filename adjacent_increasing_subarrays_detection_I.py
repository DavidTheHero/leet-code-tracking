class Solution(object):
    def hasIncreasingSubarrays(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        def is_increasing(nums, start, k):
            for i in range(start + 1, start + k):
                if nums[i-1] >= nums[i]:
                    return False
            return True
        l=0
        r=l+k
        while r+k <= len(nums):
            if is_increasing(nums, l, k) and is_increasing(nums, r, k):
                return True
            l+=1
            r=l+k
        return False

        
nums = [1,2,3,4,4,4,4,5,6,7]
k = 3
print(Solution().hasIncreasingSubarrays(nums, k))