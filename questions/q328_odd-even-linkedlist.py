'''
Given a singly linked list, group all odd nodes together
followed by the even nodes.
Please note here we are talking about the node number
and not the value in the nodes.

You should try to do it in place.
The program should run in
O(1) space complexity and
O(nodes) time complexity.

Example:
Given 1->2->3->4->5->NULL,
return 1->3->5->2->4->NULL.

Note:
The relative order inside both the even and odd groups should remain as it was in the input. 
The first node is considered odd, the second node even and so on ...

https://leetcode.com/problems/odd-even-linked-list/

referred to:
https://leetcode.com/discuss/85075/python-solution
'''
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head: return head # base case
        # **note: this states the link order of oddNodes... --links-to--> evenNodes...->NULL
        #         after all the changes in the while loop
        oddPtr = head
        evenPtr = head.next
        # run only if even node has following valued nodes to run for
        while evenPtr and evenPtr.next:
            # temp holds the next node of even's (**note: assignment to this node)
            tempPtr = evenPtr.next
            # assign the ptrs to the next nodes (**note: assigning ptrs, not the node itself!)
            evenPtr.next = evenPtr.next.next
            # used to have the latest odd node point to first even node
            tempPtr.next = oddPtr.next
            oddPtr.next = tempPtr # (**note: assigning ptr to the node for oddPtr below!)
            # actual assignment of the next odd,even nodes respectively
            # BUT oddPtr's latest node .next actually points to first even node
            evenPtr = evenPtr.next
            oddPtr = oddPtr.next
        # return linked list from head, it is changed in-place
        return head
        