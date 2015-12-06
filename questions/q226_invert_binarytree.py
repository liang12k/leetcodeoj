'''
Invert a binary tree.

     4
   /   \
  2     7
 / \   / \
1   3 6   9
to
     4
   /   \
  7     2
 / \   / \
9   6 3   1

'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root: return
        nodes=[root] # operate on the tree itself
        while nodes: # keep going thru all layers
            treelayer=[]
            for node in nodes:
                # do the swap of L/R node @ each tree layer; iterate to next tree layer & repeat
                node.left,node.right=node.right,node.left
                if node.left is not None:
                    treelayer.append(node.left)
                if node.right is not None:
                    treelayer.append(node.right)
            nodes=treelayer # this is the next layer to go thru
        return root # this tree is changed