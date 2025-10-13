class Solution(object):
    def removeAnagrams(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        i=1
        temp1=sorted(words[0])
        while i < len(words):
            temp2 = sorted(words[i])
            if temp2 == temp1:
                words.pop(i)
            else:
                temp1=temp2
                i+=1
        return words
        
words = ["abba","baba","bbaa","cd","cd"]
print(Solution().removeAnagrams(words))