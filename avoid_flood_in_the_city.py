class Solution(object):
    def avoidFlood(self, rains):
        """
        :type rains: List[int]
        :rtype: List[int]
        """
        import bisect
        n = len(rains)
        res = [-1] * n
        full = {}
        dry_day = []
        for i, lake in enumerate(rains):
            if lake > 0:
                if lake in full:
                    j = bisect.bisect_right(dry_day, full[lake])
                    if j == len(dry_day):
                        return []
                    dry_day_index = dry_day.pop(j)
                    res[dry_day_index] = lake
                full[lake] = i
                res[i] = -1
            else:
                bisect.insort(dry_day, i)
                res[i] = 1 
        return res

        
rains = [1,2,3,4]
print(Solution().avoidFlood(rains))