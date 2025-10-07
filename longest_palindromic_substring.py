class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        def expand(l,r):
            while l>=0 and r<len(s) and s[l]==s[r]:
                l-=1
                r+=1
            return s[l+1:r]
        longest = ""
        for i in range(len(s)):
            odd = expand(i, i)
            even = expand(i, i+1)
            if len(odd) > len(longest):
                longest = odd
            if len(even) > len(longest):
                longest = even
        return longest
        
s = "babad"
print(Solution().longestPalindrome(s))