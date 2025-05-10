class Solution:
    def isPalindrome(self, s):
        sen=[i.lower() for i in  s if i.isalnum()]
        return sen==sen[::-1]