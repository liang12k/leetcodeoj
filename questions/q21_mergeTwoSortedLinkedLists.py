'''
Merge two sorted linked lists and return it as a new list.
The new list should be made by splicing together the nodes of the
first two lists.
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    # @param {ListNode} l1
    # @param {ListNode} l2
    # @return {ListNode}
    def mergeTwoLists(self, l1, l2):
        newlinkedlistPtr = newlinkedlist=ListNode(0)
        while l1 and l2:
            if l1.val < l2.val:
                newlinkedlistPtr.next = l1
                l1 = l1.next
            else:
                newlinkedlistPtr.next = l2
                l2 = l2.next
            newlinkedlistPtr = newlinkedlistPtr.next
        if l1 and not l2:
            newlinkedlistPtr.next = l1
        else:
            newlinkedlistPtr.next = l2
        return newlinkedlist.next
