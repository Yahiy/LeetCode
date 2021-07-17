# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# class Solution(object):
#     def buildTree(self, preorder, inorder):
#         """
#         :type preorder: List[int]
#         :type inorder: List[int]
#         :rtype: TreeNode
#         """
#         t = TreeNode()
#         t.val = preorder[0]

#         if len(preorder)==1 and len(inorder)==1:
#             return t
#         i = 0
#         for xx in inorder:
#             i+=1
#             if xx == t.val: 
#                 break
#         in_l, in_r = inorder[:i-1], inorder[i:]  
#         print(in_l, in_r ) 
#         pre_l = [x for x in preorder if x in in_l]
#         pre_r = [x for x in preorder if x in in_r]
        
#         t.left = self.buildTree(pre_l, in_l)
#         t.right = self.buildTree(pre_r, in_r)
#         print(t)

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        def recur(root, left, right):
            if left > right: return                               # 递归终止
            node = TreeNode(preorder[root])                       # 建立根节点
            i = dic[preorder[root]]                               # 划分根节点、左子树、右子树
            node.left = recur(root + 1, left, i - 1)              # 开启左子树递归
            node.right = recur(i - left + root + 1, i + 1, right) # 开启右子树递归
            return node                                           # 回溯返回根节点

        dic, preorder = {}, preorder
        for i in range(len(inorder)):
            dic[inorder[i]] = i
        return recur(0, 0, len(inorder) - 1)
