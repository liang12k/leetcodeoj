'''
Reverse a singly linked list.
'''
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param {ListNode} head
    # @return {ListNode}
    def reverseList(self, head):
        if not head:
            return []
        newLinkedList = ListNode(0)
        newLinkedListPtr = newLinkedList
        while head:
            node = ListNode(head.val)
            node.next = newLinkedListPtr.next
            newLinkedListPtr.next = node
            head = head.next
        return newLinkedList.next
