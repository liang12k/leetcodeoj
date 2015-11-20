'''
Given a linked list, remove the nth node from the end of list
and return its head.

For example,

   Given linked list: 1->2->3->4->5, and n = 2.

   After removing the second node from the end,
   the linked list becomes 1->2->3->5.

Note:
Given n will always be valid.
Try to do this in one pass.
'''
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        '''
            using a fast-slow ptr approach
            so called 'frog-skipping'
            
            get the fast ptr to the node that'll be removed
            then when it gets to the node, determine:
            if last node, that means return empty
                **note** every n is a valid number!
            else, if there's a fast.next, have the slow ptr
            go fwd with the fast ptr going fwd
            
            when the fast ptr has reached the end,
            slow ptr has reached nth-node -1 node, need to skip the
            nth node that's next
            connect the slow ptr's node.next to the next.next
            to connect the new linked list, dropping nth-node
        '''
        slow = fast = head
        for _ in xrange(n):
            fast = fast.next
        if not fast:
            return slow.next # blank or 1-node
        while fast.next:
            fast = fast.next
            slow = slow.next
        # skip the nth-node, get its .next node
        slow.next = slow.next.next
        # don't understand, returning it as-is?
        # how to validate if o/p is correct?
        return head