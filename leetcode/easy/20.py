# def isValid(s: str) -> bool:
#     stack = []
#     mapping = {')': '(', '}': '{', ']': '['}
    
#     for char in s:
#         if char in mapping.values():  
#             stack.append(char)
#         else:  
#             if not stack or stack[-1] != mapping[char]:
#                 return False
#             stack.pop()
    
#     return not stack  

from collections import deque

class Solution:
    def isValid(self, s: str) -> bool:
        stack = deque()
        mapping = {')': '(', '}': '{', ']': '['}
        
        for char in s:
            if char in mapping.values():  
                stack.append(char)
            elif not stack or stack[-1] != mapping[char]:  
                return False
            else:  
                stack.pop()
        
        return not stack 
 