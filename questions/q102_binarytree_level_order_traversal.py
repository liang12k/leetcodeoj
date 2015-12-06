'''
Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).

For example:
Given binary tree {3,9,20,#,#,15,7},
    3
   / \
  9  20
    /  \
   15   7
return its level order traversal as:
[
  [3],
  [9,20],
  [15,7]
]
'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root is None: return []
        nodes=[root]
        ans=[[root.val]] # container of node vals @ each tree layer in order
        while nodes:
            treelayer=[]
            for node in nodes:
                nodeL,nodeR=node.left,node.right
                if nodeL is not None:
                    treelayer.append(nodeL)
                if nodeR is not None:
                    treelayer.append(nodeR)
            nodes=treelayer
            if treelayer:
                ans+=[[n.val for n in treelayer]] # add to ans tail all vals at curr layer
        return ans