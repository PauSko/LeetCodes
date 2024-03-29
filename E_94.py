#E_94
#Given the root of a binary tree, return the inorder traversal of its nodes' values.

#Example 1:
#Input: root = [1,null,2,3]
#Output: [1,3,2]

# from typing import List, Optional
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        
        inor_trav = []
        inor_trav.extend(self.inorderTraversal(root.left))
        inor_trav.append(root.val)
        inor_trav.extend(self.inorderTraversal(root.right))

        return inor_trav