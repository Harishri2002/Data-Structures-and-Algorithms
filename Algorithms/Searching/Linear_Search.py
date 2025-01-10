def LinearSearch(arr,target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

print(LinearSearch([3,4,5,6],4))
print(LinearSearch([2,3,4,5],7))

"""
Problem Statement:

Given a list of n elements with values and target element, find the index/position of the target in list.

The linear search is a basic search algorithm which searches all the elements in the list and finds the required value. 
This is also known as sequential search.

Time Complexity:

Best Case: O(1)
Average Case: O(n)
Worst Case: O(n)
"""