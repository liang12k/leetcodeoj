'''
Reverse a singly linked list.
'''
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    # @param {ListNode} head
    # @return {ListNode}
    def reverseList(self, head):
        if not head:
            return []
        new_linked_list = ListNode(0)
        new_linked_list_pointer = new_linked_list
        while head:
            node = ListNode(head.val)
            node.next = new_linked_list_pointer.next
            new_linked_list_pointer.next = node
            head = head.next
        return new_linked_list.next
