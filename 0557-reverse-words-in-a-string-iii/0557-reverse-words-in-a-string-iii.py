class Solution:
    def reverseWords(self, s: str) -> str:
        str=s.split(" ")
        reverse_str=[]
        for word in str:
            reverse=word[::-1]
            reverse_str.append(reverse)

        return ' '.join(reverse_str)

        