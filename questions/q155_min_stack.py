'''
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

push(x) -- Push element x onto stack.
pop() -- Removes the element on top of the stack.
top() -- Get the top element.
getMin() -- Retrieve the minimum element in the stack.
'''

class MinStack(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack=[]
        self.stackMin=[]
        

    def push(self, x):
        """
        :type x: int
        :rtype: nothing
        """
        self.stack.append(x)
        if self.stackMin:
            self.stackMin.append(x if x<self.stackMin[-1] else self.stackMin[-1])
        else:
            self.stackMin.append(x)
        

    def pop(self):
        """
        :rtype: nothing
        """
        if self.stack:
            self.stack.pop()
            self.stackMin.pop()
        

    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1] if self.stack else None
        

    def getMin(self):
        """
        :rtype: int
        """
        return self.stackMin[-1] if self.stackMin else None