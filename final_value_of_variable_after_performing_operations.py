class Solution(object):
    def finalValueAfterOperations(self, operations):
        """
        :type operations: List[str]
        :rtype: int
        """
        x=0
        for op in operations:
            if op == "--X":
                x-=1
            elif op == "X--":
                x-=1
            elif op == "X++":
                x+=1
            else:
                x+=1
        return x

        
operations = ["++X","++X","X++"]
print(Solution().finalValueAfterOperations(operations))