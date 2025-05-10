import sys

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    # Function to add two numbers represented by linked lists
    def addTwoNumbers(self, l1, l2):
        dummy = ListNode(0)
        current = dummy
        carry = 0

        # Traverse both lists
        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            # Calculate sum and carry
            total = val1 + val2 + carry
            carry = total // 10
            current.next = ListNode(total % 10)
            current = current.next

            # Move to the next nodes in l1 and l2
            if l1: l1 = l1.next
            if l2: l2 = l2.next

        return dummy.next

    # Zigzag Conversion
    def convert(self, s, numRows):
        if numRows == 1 or numRows >= len(s):
            return s
        
        rows = [''] * numRows
        cur_row = 0
        direction = -1

        for char in s:
            rows[cur_row] += char
            if cur_row == 0 or cur_row == numRows - 1:
                direction *= -1
            cur_row += direction
        
        return ''.join(rows)

    # Find Median of Two Sorted Arrays
    def findMedianSortedArrays(self, nums1, nums2):
        merged = sorted(nums1 + nums2)
        n = len(merged)
        if n % 2 == 1:
            return float(merged[n // 2])
        else:
            return (merged[n // 2 - 1] + merged[n // 2]) / 2.0

# Example usage
l1 = ListNode(2, ListNode(4, ListNode(3)))  # Represents 342
l2 = ListNode(5, ListNode(6, ListNode(4)))  # Represents 465
result = Solution().addTwoNumbers(l1, l2)

# Print the result as a list
output = []
while result:
    output.append(result.val)
    result = result.next
print(output)  # Output: [7, 0, 8]

# Zigzag conversion example
s = "PAYPALISHIRING"
numRows = 3
print(Solution().convert(s, numRows))  # Output: "PAHNAPLSIIGYIR"

# Find Median of Two Sorted Arrays example
nums1 = [1, 3]
nums2 = [2]
print(Solution().findMedianSortedArrays(nums1, nums2))  # Output: 2.0

nums1 = [1, 2]
nums2 = [3, 4]
print(Solution().findMedianSortedArrays(nums1, nums2))  # Output: 2.5
