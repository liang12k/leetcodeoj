'''
Given a sorted linked list, delete all duplicates such that
each element appear only once.

For example,
Given 1->1->2, return 1->2.
Given 1->1->2->3->3, return 1->2->3.
'''
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    # @param {ListNode} head
    # @return {ListNode}
    def deleteDuplicates(self, head):
        uniqlist=ListNode(0)
        uniqlistPtr=uniqlist
        currval=None
        while head:
            if head.val!=currval:
                currval=head.val
                uniqnode=ListNode(currval)
                uniqlistPtr.next=uniqnode
                uniqlistPtr=uniqnode
            head=head.next
        return uniqlist.next

# 88ms per leetcode
