'''
Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along
the shortest path from the root node down to the nearest leaf node.
'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None: return 0
        mindepth=1
        nodes=[root]
        while nodes:
            treelayer=[]
            for node in nodes:
                nodeL,nodeR=node.left,node.right
                if nodeL is None and nodeR is None:
                    return mindepth
                if nodeL is not None:
                    treelayer.append(nodeL)
                if nodeR is not None:
                    treelayer.append(nodeR)
            nodes=treelayer
            mindepth+=1
        return mindepth