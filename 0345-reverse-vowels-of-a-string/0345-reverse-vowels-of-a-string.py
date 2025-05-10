class Solution(object):
    def reverseVowels(self, s):
        vowels="aeiouAEIOU"
        vow=[c for c in s if c in vowels]
        revStr=[]
        i=0
        for char in s:
            if char in vowels:
                revStr.append(vow.pop())

            else:
                revStr.append(char)

        return ''.join(revStr)