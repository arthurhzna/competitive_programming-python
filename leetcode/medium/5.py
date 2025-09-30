# class Solution:
#     def longestPalindrome(self, s: str) -> str:
#         res = ""
#         for i in range(len(s)):
#             for j in range(i+1, len(s)+1):
#                 substring = s[i:j] 
#                 if substring == substring[::-1] and len(substring) > len(res):
#                     #aba == aba
#                     res = substring
#         return res

class Solution:###
    def longestPalindrome(self, s: str) -> str:
        def expand(left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left+1:right]  
        res = ""
        for i in range(len(s)):
            odd = expand(i, i)
            even = expand(i, i+1)
            if len(odd) > len(res):
                res = odd
            if len(even) > len(res):
                res = even
        return res


