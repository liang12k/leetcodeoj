'''
Write a program to find the node at which the intersection of
two singly linked lists begins.

A:          a1 -> a2
                   |
                   v
                  c1 -> c2 -> c3
                   ^
                   |           
B:     b1 -> b2 -> b3

Notes:
If the two linked lists have no intersection at all, return null.
The linked lists must retain their original structure after the function returns.
You may assume there are no cycles anywhere in the entire linked structure.
Your code should preferably run in O(n) time and use only O(1) memory.
'''
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if not (headA and headB): return None
        while headA or headB:
            if headA==headB: return headA
            if headA.next: headA=headA.next
            if headB.next: headB=headB.next
        return None

# Last executed input:
# No intersection: [1,3,5,7,9,11,13,15,17,19,21], [2]
