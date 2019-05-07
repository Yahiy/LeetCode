# Binary Tree Traversal without Recursion

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        
        stack Time O(n) Space O(h)
        """
        ans = [] #output
        s = []   # stack
        while(root or len(s)):
            while(root):
                s.append(root)
                root = root.left
            root = s.pop()
            ans.append(root.val)
            root = root.right
        return ans
        
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        ans = []
        s = []
        while(root or len(s)):
            while(root):
                ans.append(root.val)
                s.append(root)
                root = root.left 
            root = s.pop()
            root = root.right
        return ans
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        
        stack Time O(n) Space O(h)
        """
        ans = []
        s,f = [], []
        while(root or len(s)):
            while(root):
                s.append(root)
                f.append(0)
                root = root.left
            
            root = s.pop()
            flag = f.pop()
            if flag == 0:
                s.append(root)
                f.append(1)
                root = root.right
            else:
                ans.append(root.val)
                root = None
        return ans
