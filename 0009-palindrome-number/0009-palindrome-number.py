class Solution:
    def isPalindrome(self, x):
        # Step 1: Negative numbers or numbers ending with 0 but not equal to 0 are not palindromes
        if x < 0 or (x % 10 == 0 and x != 0):
            return False
        
        # Step 2: Reverse half of the number
        reversed_half = 0
        while x > reversed_half:
            reversed_half = reversed_half * 10 + x % 10
            x //= 10
        
        # Step 3: If x is equal to reversed_half or the number is an even length and reversed_half equals x
        return x == reversed_half or x == reversed_half // 10
