“”“
215. Kth Largest Element in an Array
Find the kth largest element in an unsorted array. Note that it is the kth largest element in the sorted order, not the kth distinct element.

Example 1:
Input: [3,2,1,5,6,4] and k = 2
Output: 5
Example 2:
Input: [3,2,3,1,2,4,5,5,6] and k = 4
Output: 4
”“”

class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        k_array = nums[:k]
        k_array.sort(reverse=True)
        
        for i in nums[k:]:
            # print(k_array)
            if i > k_array[0]:
                k_array.insert(0,i)
                k_array = k_array[:-1]
            elif i <= k_array[-1]:
                continue
            else:
                k_array = self.binary_serch(k_array,i,k)
            
        return k_array[-1]
        
    
    def binary_serch(self, array, a, k):
        # print(array,a)
        s,e = 0, k-1
        while(s<=e):
            m = (s+e)//2
            if array[m]<=a<=array[m-1] :
                array.insert(m,a)
                # print('1',array,a)
                return array[:-1]
            elif array[m+1]<=a<=array[m] :
                array.insert(m+1,a)
                # print('2',array,a)
                return array[:-1]
            if a<array[m]:
                s = m+1
            else:
                e = m-1
        
        
