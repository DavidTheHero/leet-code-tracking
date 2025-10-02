class Solution(object):
    def maxBottlesDrunk(self, numBottles, numExchange):
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
            numBottles = 0
            if empty//numExchange:
                numBottles+=1
                empty -= numExchange
                numExchange+=1
        return drink
        
numBottles = 13
numExchange = 6
print(Solution().maxBottlesDrunk(numBottles, numExchange))