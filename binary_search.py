"""
153. Find Minimum in Rotated Sorted Array
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e.,  [0,1,2,4,5,6,7] might become  [4,5,6,7,0,1,2]).

Find the minimum element.

You may assume no duplicate exists in the array.

Example 1:

Input: [3,4,5,1,2] 
Output: 1
Example 2:

Input: [4,5,6,7,0,1,2]
Output: 0
"""
#leetcode
class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        n = len(nums)
        if n == 1:
            return nums[0]
        if nums[0] < nums[-1]:
            return nums[0]
        
        s,e = 0, n-1
        mid = 0
        while(s<=e):
            mid = (s+e)/2
            if nums[mid] > nums[mid + 1]:
                return nums[mid + 1]
            if nums[mid - 1] > nums[mid]:
                return nums[mid]
            if(nums[mid] > nums[s]):
                s = mid+1
            else:
                e = mid-1
# myself
class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        n = len(nums)
        if n == 1:
            return nums[0]
        
        s,e = 0, n-1
        mid = 0
        while(s<=e):
            mid = (s+e)/2
            print(s,e,mid)
            if nums[mid] > nums[mid + 1]:
                return nums[mid + 1]
            if nums[mid - 1] > nums[mid]:
                return nums[mid]
            if nums[mid] > nums[s] and nums[mid] > nums[e]:
                s = mid+1
            else:
                e = mid-1
                
"""
33. Search in Rotated Sorted Array
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).

You are given a target value to search. If found in the array return its index, otherwise return -1.

You may assume no duplicate exists in the array.

Your algorithm's runtime complexity must be in the order of O(log n).

Example 1:

Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4
Example 2:

Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1
"""
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        t = target
        n =len(nums)
        if n == 0:
            return -1
        
        max_index = self.find_max(nums)
        print(max_index)
        
        s,e = 0,0
        if t >=nums[0]:
            s,e = 0,max_index
        else:
            s,e = max_index+1, n-1
            
        while(s<=e):
            m = (s+e)//2
            if nums[m] == t:
                return m
            if (t>nums[m]):
                s = m+1
            else:
                e = m-1
        return -1
        
    
    def find_max(self, nums):
        n = len(nums)
        if n == 1:
            return 0
        if nums[0] < nums[-1]:
            return n-1
        
        s,e = 0, n-1
        mid = 0
        while(s<=e):
            mid = (s+e)/2
            if nums[mid] > nums[mid + 1]:
                return mid
            if nums[mid - 1] > nums[mid]:
                return mid-1
            if(nums[mid] > nums[s]):
                s = mid+1
            else:
                e = mid-1
        

"""
154. Find Minimum in Rotated Sorted Array II
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e.,  [0,1,2,4,5,6,7] might become  [4,5,6,7,0,1,2]).

Find the minimum element.

The array may contain **duplicates**.

Example 1:

Input: [1,3,5]
Output: 1
Example 2:

Input: [2,2,2,0,1]
Output: 0

[1,1]
[5,1,5,5,5]
[5,5,5,1,5]

if nums[mid] == nums[s]:
    s += 1
"""
class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
                
        n = len(nums)
        if n == 1:
            return nums[0]
        if nums[0] < nums[-1]:
            return nums[0]
        
        s,e = 0, n-1
        mid = 0
        while(s<e):
            print(s,e)
            mid = (s+e)/2
            
            if nums[mid] > nums[mid + 1]:
                return nums[mid + 1]
            if nums[mid - 1] > nums[mid]:
                return nums[mid]
            if nums[mid] == nums[s]:
                s += 1
            elif nums[mid] > nums[s] and nums[mid] > nums[e]:
                s = mid+1
            else:
                e = mid-1
        if s==e:
            return nums[s]
        
"""        
540. Single Element in a Sorted Array
Medium
Share
Given a sorted array consisting of only integers where every element 
appears exactly twice except for one element which appears exactly once. 
Find this single element that appears only once.

Example 1:
Input: [1,1,2,3,3,4,4,8,8]
Output: 2
Example 2:
Input: [3,3,7,7,10,11,11]
Output: 10
"""
class Solution(object):
    def singleNonDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n == 1:
            return nums[0]
        s,e = 0, n-1
        if nums[s] != nums[s+1]:
            return nums[s]
        if nums[e] != nums[e-1]:
            return nums[e]
        
        while(s<=e):
            m = (s+e)//2
            left,mid,right = nums[m-1], nums[m], nums[m+1]
            if mid != left and mid != right :
                return nums[m]
            elif m%2 == 0 and mid==left or m%2==1 and mid==right:
                e = m-1
            else:
                s = m+1
        return None
            
      





