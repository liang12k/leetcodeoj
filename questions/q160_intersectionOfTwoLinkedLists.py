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
If the two linked lists have no intersection at all, return null (None).
The linked lists must retain their original structure after the function returns.
You may assume there are no cycles anywhere in the entire linked structure.
Your code should preferably run in O(n) time and use only O(1) memory.

O(1) space: does not depend on the size of the input.
            memory is constant in algorithm
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
        # base case: blank input(s), ignore
        if not headA or not headB: return None
        ptrA = headA
        isChangedA = False
        ptrB = headB
        isChangedB = False
        while headA or headB:
            if ptrA == ptrB: return ptrA
            ptrA = ptrA.next
            if not ptrA:
                if isChangedA: return None
                ptrA = headB
                isChangedA = True
            ptrB = ptrB.next
            if not ptrB:
                if isChangedB: return None
                ptrB = headA
                isChangedB = True
        return None

# 404ms per leetcode