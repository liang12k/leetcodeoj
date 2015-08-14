'''
Remove all elements from a linked list of integers that have value val.

Example
Given: 1 --> 2 --> 6 --> 3 --> 4 --> 5 --> 6, val = 6
Return: 1 --> 2 --> 3 --> 4 --> 5
'''
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    # @param {ListNode} head
    # @param {integer} val
    # @return {ListNode}
    def removeElements(self, head, val):
        nonvals=[]
        # idea: use a 'slow','fast' pointer; avoiding a list
        #       slow is at the current node (node.next)
        #       fast is the next node (node.next.next)
        #       slow will link w fast
        #           if it isn't val
        #           else will wait until a fast comes in non val
        while head:
            if head.val!=val:
                nonvals.append(head.val)
            head=head.next
        head=ListNode(0)
        headPtr=head
        for val in nonvals:
            node=ListNode(val)
            headPtr.next=node
            headPtr=node
        return head.next
