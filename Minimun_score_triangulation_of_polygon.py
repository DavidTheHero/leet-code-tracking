class Solution(object):
    def minScoreTriangulation(self, values):
        """
        :type values: List[int]
        :rtype: int
        """
        n = len(values)
        dp = [[0] * n for _ in range(n)]

        for length in range(3, n + 1):
            for i in range(0, n - length + 1):
                j = i + length - 1
                best = float('inf')
                for k in range(i + 1, j):
                    score = dp[i][k] + dp[k][j] + values[i] * values[k] * values[j]
                    if score < best:
                        best = score
                dp[i][j] = best # type: ignore

        return dp[0][n - 1]

values = [3, 7, 4, 5]
print(Solution().minScoreTriangulation(values))

# values = [1, 3, 1, 4, 1, 5]
# print(Solution().minScoreTriangulation(values))