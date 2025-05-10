class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        result = []
        while columnNumber:
            columnNumber -= 1
            char = chr(columnNumber % 26 + 65)
            result.append(char)
            columnNumber //= 26
        
        return ''.join(result[::-1])