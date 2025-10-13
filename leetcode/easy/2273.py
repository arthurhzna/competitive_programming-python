class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        result = []
        prev = ""
        
        for word in words:
            if sorted(word) != sorted(prev):
                result.append(word)
                prev = word
        
        return result