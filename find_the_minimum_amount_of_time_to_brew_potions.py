class Solution(object):
    def minTime(self, skill, mana):
        """
        :type skill: List[int]
        :type mana: List[int]
        :rtype: int
        """
        prefix = []
        running = 0
        for value in skill:
            running += value
            prefix.append(running)

        total_time = 0
        m = len(mana)
        for j in range(m - 1):
            delta = float("-inf")
            right = mana[j + 1]
            current = mana[j]
            for i, pref in enumerate(prefix):
                prev_pref = prefix[i - 1] if i > 0 else 0
                delta = max(delta, pref * current - prev_pref * right)
            total_time += delta

        total_time += prefix[-1] * mana[-1]
        return total_time


skill = [1, 5, 2, 4]
mana = [5, 1, 4, 2]
print(Solution().minTime(skill, mana))
