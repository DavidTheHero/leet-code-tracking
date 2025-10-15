class Solution(object):
    def maxIncreasingSubarrays(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n < 2:
            return 0

        ans = 0
        prev_len = 0
        curr_len = 1

        for i in range(1, n):
            if nums[i] > nums[i - 1]:
                curr_len += 1
            else:
                ans = max(ans, curr_len // 2)
                if prev_len:
                    ans = max(ans, min(prev_len, curr_len))
                prev_len = curr_len
                curr_len = 1

        ans = max(ans, curr_len // 2)
        if prev_len:
            ans = max(ans, min(prev_len, curr_len))

        return ans

nums = [2,5,7,8,9,2,3,4,3,1]
print(Solution().maxIncreasingSubarrays(nums))
