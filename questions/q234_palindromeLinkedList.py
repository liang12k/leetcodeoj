'''
Given a singly linked list, determine if it is a palindrome.

Follow up:
Could you do it in O(n) time and O(1) space?
'''
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    # @param {ListNode} head
    # @return {boolean}
    def isPalindrome(self, head):
        linkedlistStr = []
        while head:
            linkedlistStr.append(head.val)
            head = head.next
        return linkedlistStr == linkedlistStr[::-1]

# leetcode states 172ms
