# find the minimum length subarray, where the sum is greater than or equal to the target.
# Assume all values are positive

def shortestSubarray(nums, target):
    L, total = 0,0
    length = float('inf')

    for R in range(len(nums)):
        total+= nums[R]
        while total>= target:
            length = min(R-L+1, length)
            total-= nums[L]
            L+=1

    return 0 if length == float('inf') else length


print(shortestSubarray([1,2,3,4,5,6,2], 12))