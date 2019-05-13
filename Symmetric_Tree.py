"""
101.Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class SolutionWithoutRecusion(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        
        depth = self.TreeDepth(root)
        print(depth)
        from collections import deque
        ans = [[] for i in range(depth)]
        q, h = deque(), deque()
        q.append(root)
        h.append(1)
        while(len(q)):
            root = q.popleft()
            h_ = h.popleft()
                
            if h_ <= depth:
                if not root:
                    ans[h_-1].append(None)
                    q.append(None)
                    h.append(h_+1)
                    q.append(None)
                    h.append(h_+1)
                else: 
                    ans[h_-1].append(root.val)
                    q.append(root.left)
                    h.append(h_+1)
                    q.append(root.right)
                    h.append(h_+1)
        for i in ans:
            
            if i != i.reverse():
                return False
        return True
    
    def TreeDepth(self, root):
        if root is None:
            return 0
        if root.left is None and root.right is None:
            return 1
        if root.left is None:
            return self.TreeDepth(root.right) + 1
        if root.right is None:
            return self.TreeDepth(root.left) + 1
        else:
            return max(self.TreeDepth(root.left), self.TreeDepth(root.right)) + 1
       
    
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.isSymmetricTwo(root, root)
      
    def isSymmetricTwo(self, root1, root2):
        if root1 is None and root2 is None:
            return True
        elif root1 is not None and root2 is not None:
            if root1.val != root2.val:
                return False
            else:
                return self.isSymmetricTwo(root1.left, root2.right) and self.isSymmetricTwo(root1.right, root2.left)
        else:
            return False
        
        
        
