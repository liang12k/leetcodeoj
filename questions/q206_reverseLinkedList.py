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
        if not head: return [] # head is []
        listOfNodes=[] if head else [head]
        while head:
            listOfNodes.insert(0,ListNode(head.val))
            head=head.next
        newLinkedList=ListNode(0)
        newLinkedListPtr=newLinkedList
        for node in listOfNodes:
            newLinkedListPtr.next=node
        return newLinkedList.next

# breaking on input [1,2]
# expecting [2,1]
# returning [1]
