#E_100
#Given the roots of two binary trees p and q, write a function to check if they are the same or not.
#Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.

#Input: p = [1,2], q = [1,null,2]
#Output: false

from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        try:
            if p.val == q.val and p.left.val == q.left.val and p.right.val == q.right.val:
                return "true"
            else:
                print("false")
        except:
            print("false")

# Example 1: Two identical binary trees
p1 = TreeNode(1, TreeNode(2))
q1 = TreeNode(1,None, TreeNode(2))

print(Solution().isSameTree(p1, q1))