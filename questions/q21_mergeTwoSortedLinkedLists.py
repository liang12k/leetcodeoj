'''
Merge two sorted linked lists and return it as a new list.
The new list should be made by splicing together the nodes of the
first two lists.

ref:
http://jelices.blogspot.com/2014/05/leetcode-python-merge-two-sorted-lists.html
'''
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    # @param {ListNode} l1
    # @param {ListNode} l2
    # @return {ListNode}
    def mergeTwoLists(self, l1, l2):
        # newlinkedlist begins w a dummy node of 0 (to be skipped)
        # newlinkedlistPtr will be the obj that points to next node
        # for newlinkedlist (does all the work to create new list)
        newlinkedlist = ListNode(0)
        newlinkedlistPtr = newlinkedlist
        # keep going while there are values for l1,l2
        while l1 and l2:
            # goal is to check the node .val to determine which
            # newlinkedlistPtr.next should go to
            # by assigning the .next, it's enough to know the new
            # linked list order
            # however, to traverse thru l1,l2 need to assign the node
            # its .next node (l1=l1.next ; l2=l2.next)
            if l1.val < l2.val:
                newlinkedlistPtr.next = l1
                l1 = l1.next
            else:
                newlinkedlistPtr.next = l2
                l2 = l2.next
            # newlinkedlistPtr needs to point to its newest linked node
            # thru .next to continue adding onto the list
            newlinkedlistPtr = newlinkedlistPtr.next
        # afterwards, if there are remaining nodes left in l1 or l2,
        # need to append onto newlinkedlist by assigning
        # newlinkedlistPtr.next
        if l1 and not l2:
            newlinkedlistPtr.next = l1
        else:
            newlinkedlistPtr.next = l2
        # *note* returning newlinkedlist since newlinkedlistPtr
        #        did all the work assigning newlinkedlist's .next nodes
        #        by returning newlinkedlist.next, it skips the initial
        #        dummy ListNode(0) created and the
        #        official new merged list begins
        return newlinkedlist.next
