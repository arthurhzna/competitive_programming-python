# class Solution:
#     def isPalindrome(self, x: int) -> bool:
#         s = str(x) 
#         left = []
#         right = []
#         for i in range(len(s)):
#             left.append(s[i])

#         for i in range(len(s)):
#             right.append(s[len(s)-1-i])
#         if left == right:
#             return True
#         else:
#             return False
        
class Solution:
    def isPalindrome(self, x: int) -> bool:
        s = str(x)
        return s == s[::-1]