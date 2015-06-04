# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param {ListNode} l1
    # @param {ListNode} l2
    # @return {ListNode}
    def addTwoNumbers(self, l1, l2):
        carry = 0
        root = temp = ListNode(0)
        while l1 or l2 or carry:
            tempSum=(l1.val if l1 else 0)+(l2.val if l2 else 0)+carry
            temp.next = ListNode(tempSum % 10) # remainder, ones digit
            temp = temp.next
            carry = tempSum // 10 # get carry val (either 0 or 1)
            if l1:
                l1=l1.next
            if l2:
                l2=l2.next
        return root.next

# ref: https://leetcode.com/discuss/29326/a-python-solution