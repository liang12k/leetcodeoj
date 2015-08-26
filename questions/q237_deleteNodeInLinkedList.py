'''
Write a function to delete a node (except the tail)
in a singly linked list, given only access to that node.

Supposed the linked list is 1 -> 2 -> 3 -> 4
and you are given the third node with value 3,
the linked list should become 1 -> 2 -> 4 after calling your function.
'''
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        # if-statemnt makes sure the node isn't a single node or None
        # meaning node.next is a tail node
        if node.next:
            # linked list is 2+ nodes
            # remove the head node by getting the next node's
            # .val and .next
            node.val=node.next.val
            node.next=node.next.next
            node=node.next
        return

# 52ms per leetcode
