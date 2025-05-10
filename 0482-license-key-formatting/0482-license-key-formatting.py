class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        s=s.replace('-' , '').upper()
        result=[]
        # result=[]
        count=0
        for char in reversed(s):
            if count==k:
                result.append("-")
                count=0
            result.append(char)
            count+=1

        result=reversed(result)
        return ''.join(result)

        