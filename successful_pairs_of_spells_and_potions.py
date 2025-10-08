class Solution(object):
    def successfulPairs(self, spells, potions, success):
        """
        :type spells: List[int]
        :type potions: List[int]
        :type success: int
        :rtype: List[int]
        """
        import bisect
        pairs = []
        potions.sort()
        m = len(potions)
        for s in spells:
            need = (success+s-1)//s
            idx = bisect.bisect_left(potions, need)
            pairs.append(m-idx)
        return pairs
        

spells = [5,1,3] 
potions = [1,2,3,4,5] 
success = 7

print(Solution().successfulPairs(spells, potions, success))