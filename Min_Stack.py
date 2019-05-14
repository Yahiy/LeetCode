"""
get minimum element in the stack in time O(1)
155. Min Stack

Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

push(x) -- Push element x onto stack.
pop() -- Removes the element on top of the stack.
top() -- Get the top element.
getMin() -- Retrieve the minimum element in the stack.
"""


class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.min_stack = []
        self.min = None
        
        

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.stack.append(x)
        if self.min is None:
            self.min = x
            self.min_stack.append(x)
        else:
            if x < self.min:
                self.min = x
                self.min_stack.append(x)
            else:
                self.min_stack.append(self.min)

    def pop(self):
        """
        :rtype: None
        """
        self.stack.pop()
        self.min_stack.pop()
        if len(self.stack):
            self.min = self.min_stack[-1]
        else:
            self.min = None

    def top(self):
        """
        :rtype: int
        """
        if len(self.stack):
            return self.stack[-1]
        else:
            return None
        

    def getMin(self):
        """
        :rtype: int
        """
        if len(self.stack):
            return self.min_stack[-1]
        else:
            return None
        


# Your MinStack object will be instantiated and called as such:
obj = MinStack()
obj.push(3)
obj.pop()
param_3 = obj.top()
param_4 = obj.getMin()
