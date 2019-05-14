"""
54.Spiral Matrix
Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.

Example 1:

Input:
[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
Output: [1,2,3,6,9,8,7,4,5]
Example 2:

Input:
[
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9,10,11,12]
]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]
"""
class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        r = len(matrix)
        if r<1:
            return matrix
        c = len(matrix[0])
        
        ans = []
        s = 0 # start
        while(s*2 < c and s*2 <r):
            a = self.print_matric(matrix, s, c,r)
            ans.extend(a)
            s+=1
        return ans
    
    def print_matric(self, m, s, c,r):
        a = []
        ex, ey = c-1-s, r-1-s
        for i in range(s, c-s):
            a.append(m[s][i])
        
        for i in range(s+1,ey):
            a.append(m[i][ex])
        
        if ey>s:
            ind = range(s,ex+1)
            for i in ind[::-1]:
                a.append(m[ey][i])
        
        if ex>s:
            ind = range(s+1,ey)
            for i in ind[::-1]:
                a.append(m[i][s])
        
        return a
        
"""
59. Spiral Matrix II
Given a positive integer n, generate a square matrix filled with elements from 1 to n2 in spiral order.

Example:

Input: 3
Output:
[
 [ 1, 2, 3 ],
 [ 8, 9, 4 ],
 [ 7, 6, 5 ]
]
"""

class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        ans = [[1 for i in range(n)] for i in range(n)]
        num = 0
        for s in range(n//2+1):
            print(s)
            ans, num = self.sprial_matrix(s,ans,num)
        return ans
            
    def sprial_matrix(self,s,a,num):
        n = len(a)
        end = n-s-1
        for i in range(s, n-s):
            num+=1
            a[s][i] = num
            
        for i in range(s+1,end):
            num+=1
            a[i][end] = num
        
        if end>s:
            ind = range(s,n-s)
            for i in ind[::-1]:
                num+=1
                a[end][i] = num
        
        if end>s:
            ind = range(s+1,end)
            for i in ind[::-1]:
                num+=1
                a[i][s] = num
        return a,num
        


