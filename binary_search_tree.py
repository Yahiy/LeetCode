"""
230. Kth Smallest Element in a BST
Medium
Given a binary search tree, write a function kthSmallest to find the kth smallest element in it.
Note: 
You may assume k is always valid, 1 ≤ k ≤ BST's total elements.

Example 1:
Input: root = [3,1,4,null,2], k = 1
   3
  / \
 1   4
  \
   2
Output: 1
Example 2:
Input: root = [5,3,6,2,4,null,null,1], k = 3
       5
      / \
     3   6
    / \
   2   4
  /
 1
Output: 3
Follow up:
What if the BST is modified (insert/delete operations) often
and you need to find the kth smallest frequently? How would you optimize the kthSmallest routine?
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        ans = self.inorderTraversal(root,k)
        return ans[-1]
   
   def kthSmallest2(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        ans = [] #output
        s = []   # stack
        while root or len(s):
            while root:
                s.append(root)
                root = root.left
            root = s.pop()
            ans.append(root.val)
            if len(ans) == k:
                return root.val
            root = root.right
        
    def inorderTraversal(self, root, k):
        """
        :type root: TreeNode
        :rtype: List[int]
        
        stack Time O(n) Space O(h)
        """
        ans = [] #output
        s = []   # stack
        while root or len(s):
            while root:
                s.append(root)
                root = root.left
            root = s.pop()
            ans.append(root.val)
            if len(ans) >= k:
                break
            root = root.right
        return ans
        
