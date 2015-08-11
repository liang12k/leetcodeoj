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
        # base case, return blank
        if not head:
            return []
        # create the linked list that'll be returned and a
        # pointer for this linked list to point to following nodes
        # -new_linked_list_pointer to link from as a temp head node
        new_linked_list = ListNode(0)
        new_linked_list_pointer = new_linked_list
        # ---------------------------------------------
        # approach:
        #   going thru entire linked list head,
        #   create a new node by ListNode for the current val
        #   assign its .next to current new_linked_list_pointer.next
        #   as this node needs to take in all the latest
        #   new_linked_list_pointer linked values
        #   then assign new_linked_list_pointer.next to current node
        #   to update the new_linked_list with latest head node
        #
        #   eg:
        #       [0 | ] --> None : new_linked_list (pointer going to None)
        #
        #       [1 | ] --> [2 | ] is the input 'head'
        #
        #       iterating thru input linked list 'head'
        #
        #       @ [1 | ] : node.next = new_linked_list_pointer.next
        #       need to let node take the latest new_linked_list link
        #       [1 | ] --> None
        #
        #       new_linked_list_pointer.next = node
        #       update new_linked_list with latest head node [1 | ]
        #       [0 | ] --> [1 | ] --> None
        #
        #       @ [2 | ] : node.next = new_linked_list_pointer.next
        #       need to let node take the latest new_linked_list link
        #       [2 | ] --> [1 | ] --> None
        #
        #       new_linked_list_pointer.next = node
        #       update new_linked_list with latest head node [2 | ]
        #       [0 | ] --> [2 | ] --> [1 | ] --> None
        #
        #       ...
        #
        #   continue thru linked list head
        #
        # ---------------------------------------------
        # go thru linked list head
        while head:
            # create a new ListNode at latest val
            node = ListNode(head.val)
            # need to let node take the latest new_linked_list link
            node.next = new_linked_list_pointer.next
            # update new_linked_list with latest head node
            new_linked_list_pointer.next = node
            head = head.next
        # returning new_linked_list.next skips the dummy ListNode(0)
        # that's used as a placeholder for new_linked_list_pointer
        # to link from as a temp head node
        return new_linked_list.next
