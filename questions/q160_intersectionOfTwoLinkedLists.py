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

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        # approach:
        #     having 2 linked lists, pointers for each list
        #     let each pointer go thru their respective list
        #     for the shorter list, its pointer will change (cross)
        #     over to the other list
        #     continuing the traversal, the other pointer will reach its
        #     end of list and cross over to the other list
        #     at this point, both pointers will begin at the 'same index'
        #     this traversal will actually determine if there's an
        #     intersection between the 2 lists (Y-linked list)
        #     **note**
        #         an intersection here means both lists merge at a certain
        #         node, hence Y-shaped linked list
        #     
        #     eg:
        #         len headA > len headB
        #         therefore, after ptrB crosses to headA, ptrA crosses to headB
        #         this means ptrA,ptrB begin at equivalent index as if both
        #         linked lists have same len
        #         
        #         headA: 1->3->4->5->x
        #         headB: 2->4->x
        #         
        #         ptrA : 1
        #         ptrB : 2
        #         
        #         ptrA : 3
        #         ptrB : 4
        #         
        #         ptrA : 5
        #         ptrB : x
        #         
        #         ptrA : x
        #         ptrB : 1 -> goes to headA, bool flag set for the 'cross'
        #         
        #         **note**
        #             the real traversal begins for finding intersection
        #             as ptrB begin at an index equivalent to headB len
        #
        #         ptrA : 2 -> goes to headB, bool flag set for the 'cross'
        #         ptrB : 3
        #         
        #         ptrA : 4
        #         ptrB : 4
        # 
        # base case: blank input(s), ignore
        if not headA or not headB: return None
        # set the pointers for headA, headB
        # and bool flag when either pointer changes lists
        ptrA = headA
        isChangedA = False
        ptrB = headB
        isChangedB = False
        # (IMPROVE) keep going over the linked lists headA,headB
        while headA or headB:
            # return either ptrA,ptrB as they're the same
            if ptrA == ptrB: return ptrA
            # traverse thru headA
            ptrA = ptrA.next
            if not ptrA:
                # if the cross happened, avoid repeat, intersection DNE
                if isChangedA: return None
                # cross ptrA to headB
                ptrA = headB
                # set bool flag as ptrA has crossed to headB list
                isChangedA = True
            # traverse thru headB
            ptrB = ptrB.next
            if not ptrB:
                # if the cross happened, avoid repeat, intersection DNE
                if isChangedB: return None
                # cross ptrA to headB
                ptrB = headA
                # set bool flag as ptrA has crossed to headB list
                isChangedB = True
        # defaults, intersection DNE; should be caught in while-loop
        return None

# 404ms per leetcode