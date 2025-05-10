class Node:
    def __init__(self, val: int, left: Optional['Node'] = None, right: Optional['Node'] = None):
        self.val = val
        self.left = left
        self.right = right

class SegmentTree:

    @staticmethod
    def construct(nums: List[int], left: int, right: int) -> Node:
        if left == right:
            return Node(nums[left])
        
        mid = (left + right) // 2
        leftMax = SegmentTree.construct(nums, left, mid)
        rightMax = SegmentTree.construct(nums, mid+1, right)

        return Node(
            max(leftMax.val, rightMax.val),
            leftMax,
            rightMax
        )

    @staticmethod
    def maxQuery(head: Node, left: int, right: int, queryLeft: int, queryRight: int) -> int:
        if queryLeft > right or queryRight < left:
            return -math.inf

        if queryLeft <= left and queryRight >= right:
            return head.val

        mid = (left + right) // 2
        return max(
            SegmentTree.maxQuery(head.left, left, mid, queryLeft, queryRight),
            SegmentTree.maxQuery(head.right, mid+1, right, queryLeft, queryRight)
        )

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        length = len(nums)
        segmentTree = SegmentTree.construct(nums, 0, length - 1)
        res = []
        for left in range(length - k + 1):
            right = left + k - 1
            res.append(SegmentTree.maxQuery(segmentTree, 0, length -1, left, right))
        
        return res