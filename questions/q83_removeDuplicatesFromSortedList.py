'''
Given a sorted linked list, delete all duplicates such that
each element appear only once.

For example,
Given 1->1->2, return 1->2.
Given 1->1->2->3->3, return 1->2->3.
'''
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    # @param {ListNode} head
    # @return {ListNode}
    def deleteDuplicates(self, head):
        # new linkedlist w dummy value 0
        # and create new pointer for it
        uniqlist = ListNode(0)
        uniqlistPtr = uniqlist
        # var to determine the latest value
        # *note* helps w sorted list, dict needed for random vals
        currval = None
        while head:
            if head.val != currval:
                # take latest val
                currval = head.val
                # new node of unique val
                uniqnode = ListNode(currval)
                # point the new linkedlist ptr to this new node
                uniqlistPtr.next = uniqnode
                # assign the ptr to new node as this will
                # have its .next assigned later
                uniqlistPtr = uniqnode
            # nonetheless, traverse thru the input linkedlist
            head = head.next
        # return the linkedlist after the dummy value 0
        return uniqlist.next

# 88ms per leetcode
