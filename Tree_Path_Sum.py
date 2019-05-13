"""
postorder traversal of tree ,depth-first search

112. Path Sum
Given a binary tree and a sum, determine if the tree has a root-to-leaf path such that adding up all the values along the path equals the given sum.

Note: A leaf is a node with no children.

Example:

Given the below binary tree and sum = 22,

      5
     / \
    4   8
   /   / \
  11  13  4
 /  \      \
7    2      1
return true, as there exist a root-to-leaf path 5->4->11->2 which sum is 22.
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def hasPathSum(self, root, sum_):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        ans = []
        s,f = [], []
        while(root or len(s)):
            while(root):
                s.append(root)
                ans.append(root.val)
                f.append(0)            
                root = root.left
            
            root = s.pop()
            flag = f.pop()
            ans.pop()
            if flag == 0:
                s.append(root)
                ans.append(root.val)
                if root.left is None and root.right is None:
                    if sum(ans) == sum_:
                        return True
                f.append(1)
                root = root.right
            else:
                root = None
        return False
        
"""
113. Path Sum II
Given a binary tree and a sum, find all root-to-leaf paths where each path's sum equals the given sum.

Note: A leaf is a node with no children.

Example:

Given the below binary tree and sum = 22,

      5
     / \
    4   8
   /   / \
  11  13  4
 /  \    / \
7    2  5   1
Return:

[
   [5,4,11,2],
   [5,8,4,5]
]
"""
class Solution(object):
    def pathSum(self, root, sum_):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        ans = []
        s,f,v = [], [], []
        while(root or len(s)):
            while(root):
                s.append(root)
                v.append(root.val)
                f.append(0)   
                root = root.left
            
            root = s.pop()
            flag = f.pop()
            v.pop()
            if flag == 0:
                s.append(root)
                v.append(root.val)
                if root.left is None and root.right is None:
                    if sum(v) == sum_:
                        ans.append([x for x in v])
                f.append(1)
                root = root.right
            else:
                root = None
        return ans
        
"""
You are given a binary tree in which each node contains an integer value.

Find the number of paths that sum to a given value.

The path does not need to start or end at the root or a leaf, but it must go downwards (traveling only from parent nodes to child nodes).

The tree has no more than 1,000 nodes and the values are in the range -1,000,000 to 1,000,000.

Example:

root = [10,5,-3,3,2,null,11,3,-2,null,1], sum = 8

      10
     /  \
    5   -3
   / \    \
  3   2   11
 / \   \
3  -2   1

Return 3. The paths that sum to 8 are:

1.  5 -> 3
2.  5 -> 2 -> 1
3. -3 -> 11
"""
class Solution(object):
    def pathSum(self, root, sum_):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        ans = 0
        s,f,v = [], [], []
        while(root or len(s)):
            while(root):
                s.append(root)
                v.append(root.val)
                f.append(0)   
                root = root.left
            
            root = s.pop()
            flag = f.pop()
            v.pop()
            if flag == 0:
                s.append(root)
                v.append(root.val)
                f.append(1)
                root = root.right
            else:
                ans+=self.has_sum( v, root.val,sum_)
                root = None
        return ans
    
    def has_sum(self,v,val,s):
        path_num = 0
        if val == s:
            path_num += 1
        for i in v[::-1]:
            val += i
            if val == s:
                path_num += 1
        return path_num

"""
257. Binary Tree Paths
Given a binary tree, return all root-to-leaf paths.

Note: A leaf is a node with no children.

Example:

Input:

   1
 /   \
2     3
 \
  5

Output: ["1->2->5", "1->3"]

Explanation: All root-to-leaf paths are: 1->2->5, 1->3
"""
class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        ans = []
        s,f,v = [], [], []
        while(root or len(s)):
            while(root):
                s.append(root)
                v.append(root.val)
                f.append(0)   
                root = root.left
            
            root = s.pop()
            flag = f.pop()
            v.pop()
            if flag == 0:
                s.append(root)
                v.append(root.val)
                if root.left is None and root.right is None:
                        ans.append('->'.join(map(str,v)))
                f.append(1)
                root = root.right
            else:
                root = None
        return ans
