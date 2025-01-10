def MaxSubarry(nums):
    max_sum = float('-inf')
    current_sum = 0
    for i in range(len(nums)):
        current_sum += nums[i]
        
        max_sum = max(max_sum, current_sum)
        
        if current_sum < 0:
            current_sum = 0
    return max_sum

nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print(MaxSubarry(nums))

    """
    Kadane's algorithm is a dynamic programming technique used to find the maximum subarray sum within 
    a one-dimensional array. It efficiently computes the maximum sum of a contiguous subarray, and its simplicity 
    and effectiveness make it a popular choice for solving related problems.

    """