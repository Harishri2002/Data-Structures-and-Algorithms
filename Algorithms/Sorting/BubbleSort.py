def BubbleSort(nums):
    for i in range(len(nums)-1):
        for j in range(len(nums)-i-1):
            if nums[j] > nums[j+1]:
                nums[j],nums[j+1] = nums[j+1],nums[j]
    return nums

print(BubbleSort([4,3,5,6,7,1,2,10]))

# Worst and Average Case Time Complexity: O(n*n).
# Best Case Time Complexity: O(n*n).

# //Optimized BubbleSort

def optimizedBubbleSort(arr):
    n = len(arr)
    for i in range(n-1):
        swap = False
        for j in range(n-i-1):
            if arr[j] > arr[j+1]: # Swap if the element found is greater than the next element.
                arr[j],arr[j+1] = arr[j+1],arr[j]
                swap = True
        if swap == False: # IF no two elements were swapped by inner loop, then break. (It is the case when the array is already sorted)
            break
    return arr

print(optimizedBubbleSort([4,3,5,6,7,1,2,10]))

"""
    Implements an optimized version of Bubble Sort to sort a list in ascending order.
    The algorithm stops early if the array is already sorted.
    
    Args:
        arr (list): The list of numbers to be sorted.

    Returns:
        list: A new list sorted in ascending order.
"""

# Worst and Average Case Time Complexity: O(n*n). 
# Best Case Time Complexity: O(n).