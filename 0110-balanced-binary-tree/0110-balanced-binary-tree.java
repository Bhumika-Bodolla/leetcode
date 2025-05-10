/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    public int height(TreeNode root){
        if(root==null) return 0;//taking the height of null to be 0
        return 1+Math.max(height(root.left),height(root.right));//calculating the height of the node using recursion
    }
    public boolean isBalanced(TreeNode root) {
        if(root==null)//if the node is null it means that while traversing we have come to the end of the tree and so it is true that the tree is balanced
        return true;
        if(Math.abs(height(root.left)-height(root.right))>1)//calculating the height difference of the left and the right node
         return false;
        boolean l=isBalanced(root.left);//checking if both the right and the right subtree are balanced or not
        boolean r=isBalanced(root.right);
        return l&&r;//using and to return true if both the left and right subtrees are balanced
    }
}