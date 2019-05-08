"""
105.Given preorder and inorder traversal of a tree, construct the binary tree.

Note:
You may assume that duplicates do not exist in the tree.

For example, given

preorder = [3,9,20,15,7]
inorder = [9,3,15,20,7]
Return the following binary tree:

    3
   / \
  9  20
    /  \
   15   7
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if not len(preorder):
            return None
        if len(preorder) == 1:
            root = TreeNode(preorder[0])
            return root
        else:
            root = TreeNode(preorder[0])
            i = inorder.index(preorder[0])
            li = inorder[:i]
            ri = inorder[i+1:]
            lp = preorder[1:i+1]
            rp = preorder[i+1:]
            root.left = self.buildTree(lp,li)
            root.right = self.buildTree(rp,ri)
        return root
    
"""
106.Given inorder and postorder traversal of a tree, construct the binary tree.

Note:
You may assume that duplicates do not exist in the tree.

For example, given

inorder = [9,3,15,20,7]
postorder = [9,15,7,20,3]
Return the following binary tree:

    3
   / \
  9  20
    /  \
   15   7
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        if not len(postorder):
            return None
        if len(postorder) == 1:
            root = TreeNode(postorder[-1])
            return root
        else:
            root = TreeNode(postorder[-1])
            i = inorder.index(postorder[-1])
            li = inorder[:i]
            ri = inorder[i+1:]
            lp = postorder[:i]
            rp = postorder[i:-1]
            root.left = self.buildTree(li, lp)
            root.right = self.buildTree(ri, rp)
        return root
        
