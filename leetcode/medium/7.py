# class Solution:
#     def reverse(self, x: int) -> int:
#         INT_MAX = 2**31 - 1
#         INT_MIN = -2**31
#         rev = 0
#         sign = -1 if x < 0 else 1
#         x = abs(x)
#         while x != 0:
#             pop = x % 10       
#             x = x // 10        
#             if rev > (INT_MAX - pop) // 10:
#                 return 0
            
#             rev = rev * 10 + pop
        
#         return sign * rev
# // dapat digit terakhir % 10
# // dapat bilangan setelah digit terkahir di hapus // 10
# // tambahkan nilainya ke 10 100 1000 dst, yaitu di * 10 + digit terakhir

class Solution:
    def reverse(self, x: int) -> int:
        INT_MAX, INT_MIN = 2**31 - 1, -2**31
        sign = -1 if x < 0 else 1
        rev = int(str(abs(x))[::-1])
        if INT_MIN<rev<INT_MAX:
            return sign *rev
        else:
            return 0
