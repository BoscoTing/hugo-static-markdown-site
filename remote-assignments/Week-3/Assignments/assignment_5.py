def twoSum(nums, target):
    i = 0 
    right = len(nums) 
    for num in nums: 
        diff = target - num 
        left = i 
        while left < right: 
            mid = (left+right) // 2 
            if nums[mid] < diff: 
                left += 1
            elif nums[mid] > diff: 
                right -= 1 
            elif nums[mid-1] == diff:
                right -= 1
            else: 
                return [i, mid]
        i += 1 
    return "Can't find the answer." 

# time-complexity: 
# O(nlog n) + O(n) + O(1)
# Big O = nlog n
