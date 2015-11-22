'''
Write a program to find the node at which the intersection of
two singly linked lists begins. (Y-linked list)

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

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        a=headA
        b=headB
        lenA=0
        lenB=0
        # first get the len of each linked list
        while a:
            a=a.next
            lenA+=1
        while b:
            b=b.next
            lenB+=1
        # reset the ptrs to orig linked lists
        a=headA
        b=headB
        # while the lens exist, get both to an equal starting node
        # ^ determined when the len are equal
        while lenA>0 and lenB>0:
            if lenA<lenB:
                b=b.next
                lenB-=1
            if lenA>lenB:
                a=a.next
                lenA-=1
            if lenA==lenB:
                if a==b: return a # intersection
                # keep decrementing
                a=a.next
                b=b.next
                lenA-=1
                lenB-=1
        return # default