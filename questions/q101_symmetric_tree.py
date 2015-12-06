'''
Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).

For example, this binary tree is symmetric:

    1
   / \
  2   2
 / \ / \
3  4 4  3
But the following is not:
    1
   / \
  2   2
   \   \
   3    3

'''

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
        if not root: return True
        nodes=[root]
        while nodes:
            treelayerNodes=[] # container to for layer of nodes
            treelayerVals=[]  # container to determine the node vals & blanks at each layer
            for node in nodes:
                nodeL,nodeR=node.left,node.right
                if nodeL is not None:
                    treelayerNodes.append(nodeL)
                    treelayerVals.append(nodeL.val)
                else:
                    treelayerVals.append(None)
                if nodeR is not None:
                    treelayerNodes.append(nodeR)
                    treelayerVals.append(nodeR.val)
                else:
                    treelayerVals.append(None)
            if set(treelayerVals)==set([None]): return True # if blank layer, end reached
            # detect unbalanced len or unmatching vals reversed
            if len(treelayerVals)%2 or treelayerVals!=treelayerVals[::-1]: return False
            nodes=treelayerNodes
        return True