#!/usr/bin/env python
#-*-coding:utf-8-*-
import numpy as np
def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) / 2]

    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    
    return quicksort(left) + middle + quicksort(right)

print quicksort([3,6,8,32,10,1,-2,1])




def partition(array, beg, end):
    pivot_index = beg
    pivot = array[pivot_index]

    left = pivot_index + 1
    right = end - 1

    while True:
        while left <= right and array[left] < pivot:
            left += 1

        while right >= left and array[right] >= pivot:
            right -= 1

        if left > right:
            break
        else:
            array[left], array[right] = array[right], array[left]
    array[pivot_index], array[right] = array[right], array[pivot_index]

    return right

def quicksort_inplace(array, beg, end):
    if beg<end:
        pivot = partition(array, beg, end)
        quicksort_inplace(array,beg, pivot)
        quicksort_inplace(array, pivot+1, end)

    return array


def  counting_sort(arr, max_val):
	b = [0]*(max_val+1)

	for i, a in enumerate(arr):
		b[a] += 1
	sorted_index = 0
	for i in range(max_val+1):
		while b[i]>0:
			arr[sorted_index]=i
			sorted_index+=1
			b[i]-=1
	return arr

def merge(left,right):
	result = []
	while left and right:
		if left[0] <= right[0]:
			result.append(left.pop(0))
		else:
			result.append(right.pop(0))
	while left:
		result.append(left.pop(0))
	while right:
		result.append(right.pop(0))
	return result

def merge_sort(arr):
	import math
	if len(arr)<2:
		return arr
	middle = len(arr)//2
	left, right = arr[:middle], arr[middle:]
	return merge(merge_sort(left), merge_sort(right))



a = list(np.random.randint(20,size=20))
print(a)
print(merge_sort(a))
# print(quicksort_inplace(a,0,len(a)))
print(counting_sort(a,max(a)))

