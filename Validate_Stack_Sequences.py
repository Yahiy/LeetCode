"""
946. Validate Stack Sequences
Given two sequences pushed and popped with distinct values, 
return true if and only if this could have been the result of a sequence of push 
and pop operations on an initially empty stack.

Example 1:

Input: pushed = [1,2,3,4,5], popped = [4,5,3,2,1]
Output: true
Explanation: We might do the following sequence:
push(1), push(2), push(3), push(4), pop() -> 4,
push(5), pop() -> 5, pop() -> 3, pop() -> 2, pop() -> 1
Example 2:

Input: pushed = [1,2,3,4,5], popped = [4,3,5,1,2]
Output: false
Explanation: 1 cannot be popped before 2.
"""
class Solution(object):
    def validateStackSequences(self, pushed, popped):
        """
        :type pushed: List[int]
        :type popped: List[int]
        :rtype: bool
        """
        from collections import deque
        pushed, popped = deque(pushed), deque(popped)
        stack = []
        while len(popped) != 0:
            # print(stack)
            if len(stack):
                if stack[-1] == popped[0]:
                    stack.pop()
                    popped.popleft()
                elif len(pushed):
                    stack.append(pushed.popleft())
                else:
                    return False
            else:
                if len(pushed):
                    stack.append(pushed.popleft())
                else:
                    return False
        if len(stack):
            return False
        return True

            
       
