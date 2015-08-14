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
        # list to hold the node values
        # *note* making a string isn't a good idea
        #        ex. input [-1,-1] is a palindrome
        #            but checking it as a str fails
        linkedlistStr = []
        while head:
            linkedlistStr.append(head.val)
            head = head.next
        # return bool on list comparison
        # idea: avoid [::-1] as it uses addt'l space
        return linkedlistStr == list(reversed(linkedlistStr))

# leetcode states 168ms
