class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        row1=set("qwertyuiop")
        row2=set("asdfghjkl")
        row3=set("zxcvbnm")
        result=[]
        for char in words:
            lower=set(char.lower())
            if lower<=row1 or lower<=row2 or lower<=row3:
                result.append(char)

        return result


        