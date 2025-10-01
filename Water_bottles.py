class Solution(object):
    def numWaterBottles(self, numBottles, numExchange):
        """
        :type numBottles: int
        :type numExchange: int
        :rtype: int
        """
        empty = 0
        drink = 0
        while numBottles > 0 :
            drink += numBottles
            empty += numBottles
            numBottles = empty // numExchange
            empty = empty%numExchange
        return drink
        
numBottles = 15
numExchange = 4
print(Solution().numWaterBottles(numBottles, numExchange))