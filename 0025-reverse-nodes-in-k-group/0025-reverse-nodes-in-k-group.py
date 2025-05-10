from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # Step 1: Check if there are at least k nodes
        temp = head
        count = 0
        while temp and count < k:
            temp = temp.next
            count += 1
        
        if count < k:
            return head  # Not enough nodes to reverse, return as is

        # Step 2: Reverse k nodes
        prev, curr = None, head
        for _ in range(k):
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node

        # Step 3: Recursively process the remaining list
        head.next = self.reverseKGroup(curr, k)

        return prev  # New head of the reversed group
