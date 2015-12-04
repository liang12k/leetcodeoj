'''
Given two binary trees, write a function to check if
they are equal or not.

Two binary trees are considered equal if they are
structurally identical and the nodes have the same value.
'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        # check the base cases for empty nodes cases < and, or >
        if p is None and q is None: return True
        if (p is None and q is not None) or (p is not None and q is None): return False
        if p.val!=q.val: return False # at this pt, there exists p,q, depth 0, enough to check if same vals
        pnodes=[p]
        qnodes=[q]
        while pnodes and qnodes:
            # approach: have list of nodes, list of (nodeCounter,nodeValue)
            #           as node objs have diff ref addrs, using a counter for each node encountered
            #           ^ need to check this list of (nodeCounter,nodeValue), not the list of nodes
            #           reset these values each time to keep track @ each layer
            treelayerPnodes=[]
            treelayerPctrvals=[]
            pnodectr=0
            treelayerQnodes=[]
            treelayerQctrvals=[]
            qnodectr=0
            # iterate thru each p,q respectively
            # if there is a L/R node, keep track of that node and the (nodeCounter,nodeValue) separately
            # else no node to append, (None,None) used
            # incr counter nonetheless to cont. sequence to track nodes
            for pnode in pnodes:
                pnodeL,pnodeR=pnode.left,pnode.right
                if pnodeL is not None:
                    treelayerPnodes.append(pnodeL)
                    treelayerPctrvals.append((pnodectr,pnodeL.val))
                else:
                    treelayerPctrvals.append((None,None))
                if pnodeR is not None:
                    treelayerPnodes.append(pnodeR)
                    treelayerPctrvals.append((pnodectr,pnodeR.val))
                else:
                    treelayerPctrvals.append((None,None))
                pnodectr+=1
            for qnode in qnodes:
                qnodeL,qnodeR=qnode.left,qnode.right
                if qnodeL is not None:
                    treelayerQnodes.append(qnodeL)
                    treelayerQctrvals.append((qnodectr,qnodeL.val))
                else:
                    treelayerQctrvals.append((None,None))
                if qnodeR is not None:
                    treelayerQnodes.append(qnodeR)
                    treelayerQctrvals.append((qnodectr,qnodeR.val))
                else:
                    treelayerQctrvals.append((None,None))
                qnodectr+=1
            # cmp the list of (nodeCounter,nodeVals) as list of nodes have diff ref addrs
            if treelayerPctrvals!=treelayerQctrvals: return False
            # assign to keep the while-loop going
            pnodes=treelayerPnodes
            qnodes=treelayerQnodes
        return True # default trees match