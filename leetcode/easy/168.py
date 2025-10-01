class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        result = []
        while columnNumber > 0:
            columnNumber -= 1
            #agar nilai columnNumber=1 itu = A karena di tambah pada + ord('A') dibawah
            result.append(chr((columnNumber % 26) + ord('A')))
            columnNumber //= 26 # untuk digit selanjutnya karena z = 26, maka di bagi 26
        return ''.join(reversed(result))
