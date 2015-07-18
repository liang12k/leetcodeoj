# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# ref: https://leetcode.com/discuss/29326/a-python-solution

class Solution(object):
    # @param {ListNode} l1
    # @param {ListNode} l2
    # @return {ListNode}
    def addTwoNumbers(self, l1, l2):
        carry = 0
        root = temp = ListNode(0)
        while l1 or l2 or carry:
            tempSum = (l1.val if l1 else 0) + (l2.val if l2 else 0) + carry
            # remainder, ones digit
            temp.next = ListNode(tempSum % 10)
            # assignment order, can't do it all on Line16
            temp = temp.next
            # get carry val (either 0 or 1)
            carry = tempSum // 10
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        return root.next
