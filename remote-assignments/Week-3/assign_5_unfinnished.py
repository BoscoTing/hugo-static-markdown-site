from Assignments.binary_search_first import binary_search_first

def twoSum2(nums, target):
    target_position = binary_search_first(nums, target) # nlognC
    i = 0 
    for num in nums:
        if num*2 == target:
            return [i, i+1]
        diff = target - num 
        if diff < target:
            left = i
            right = target_position
        elif diff > target:
            left = target_position 
            right = len(nums)
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

# time-comlexity: 
# O(nlogn) + O(n) + O(1)
# Big O = nlogn