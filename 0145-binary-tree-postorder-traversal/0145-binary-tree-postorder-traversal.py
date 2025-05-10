class Solution:
    def postorderTraversal(self, rt: TreeNode) -> list[int]:

        if not rt: return []

        return (self.postorderTraversal(rt.left) + 
                    self.postorderTraversal(rt.right)+[rt.val])
        