def binary_search_first(numbers, 
                        target):
    left = 0
    right = len(numbers)
    while left < right:
        # print(left, right)
        mid = (left+right) // 2
        if numbers[mid] < target: 
            left += 1
        elif numbers[mid] > target: 
            right -= 1
        elif numbers[mid-1] == target:
            right -= 1
        else: # numbers[mid] == target
            return mid
    # print(left, right)
    return mid+1 # left==right時
