class Solution(object):
    def maximumEnergy(self, energy, k):
        """
        :type energy: List[int]
        :type k: int
        :rtype: int
        """
        frame = energy[:]
        for i in range(len(energy)-1-k, -1, -1):
            frame[i]+=frame[i+k]
        return max(frame)
        
energy = [5,2,-10,-5,1] 
k = 3
print(Solution().maximumEnergy(energy, k))