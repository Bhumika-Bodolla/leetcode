class Solution:
    def myAtoi(self, s):
        # Step 1: Remove leading whitespaces
        s = s.lstrip()

        # Step 2: Handle the sign (positive or negative)
        if not s:
            return 0  # return 0 if string is empty after trimming whitespaces
        sign = 1  # Assume positive by default
        if s[0] == '-':
            sign = -1
            s = s[1:]
        elif s[0] == '+':
            s = s[1:]

        # Step 3: Read the number
        num = 0
        for char in s:
            if char.isdigit():
                num = num * 10 + int(char)
            else:
                break

        # Step 4: Apply the sign to the number
        num *= sign

        # Step 5: Handle overflow/underflow within the 32-bit signed integer range
        INT_MIN, INT_MAX = -2**31, 2**31 - 1
        if num < INT_MIN:
            return INT_MIN
        if num > INT_MAX:
            return INT_MAX

        return num
