'''
Given a binary tree and a sum, determine if the tree has a
root-to-leaf path such that adding up all the values along
the path equals the given sum.

For example:
Given the below binary tree and sum = 22,
              5
             / \
            4   8
           /   / \
          11  13  4
         /  \      \
        7    2      1
return true, as there exist a root-to-leaf path 5->4->11->2
which sum is 22.
'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def hasPathSum(self, root, tgt):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if root is None: return False # base case
        nodes=[root]
        sums=[root.val]
        # nodes is a list of node @ each layer, while-loop will go thru each layer as nodes list updates per layer
        while nodes:
            # approach to go thru tree layer by layer, each layer have its nodes and sums respectively (zip)
            treelayernodes=[]
            treelayersums=[]
            for node,summ in zip(nodes,sums): # using itertools.izip will be faster (generator)
                # @ each layer, check each node's L/R
                leftnode,rightnode=node.left,node.right
                # if no L/R, no children left, end of branch, check if sum by this node is the tgt sum
                if leftnode is None and rightnode is None and summ==tgt: return True
                # add in L/R nodes if they exist w respective latest summ reaching the node
                if leftnode is not None:
                    treelayernodes.append(leftnode)
                    treelayersums.append(leftnode.val + summ)
                if rightnode is not None:
                    treelayernodes.append(rightnode)
                    treelayersums.append(rightnode.val + summ)
            # update the latest layer of nodes and sums for while and for-loop
            nodes=treelayernodes
            sums=treelayersums
        # checked all layers, no sums==tgt
        return False