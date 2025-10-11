class Solution(object):
    def maximumTotalDamage(self, power):
        """
        :type power: List[int]
        :rtype: int
        """
        from collections import Counter
        from bisect import bisect_right
        if not power:
            return 0

        cnt = Counter(power)
        vals = sorted(cnt)
        gain = [v * cnt[v] for v in vals]

        k = len(vals)
        dp = [0] * k

        for i in range(k):
            j = bisect_right(vals, vals[i] - 3) - 1
            take = gain[i] + (dp[j] if j >= 0 else 0)
            skip = dp[i - 1] if i > 0 else 0
            dp[i] = max(skip, take)

        return dp[-1]
        
power = [1,1,3,4]
print(Solution().maximumTotalDamage(power))