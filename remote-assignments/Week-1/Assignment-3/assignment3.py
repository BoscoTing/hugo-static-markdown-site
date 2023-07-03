def find_max(numbers):
  max_number = 0
  for i in numbers:
      if i > max_number:
          max_number = i
  return max_number

def find_position(
        numbers, target):
    t = 0
    result = -1
    for num in numbers:
        if num == target:
            result = t
            break
        t += 1
    return result

# 舊版
""" 
def find_position(numbers, 
                  target):
    success, fail, t = 0, 0, 0
    for num in numbers:
        if num == target:
            success += 1 
            break
        if num != target:
            fail += 1
        t += 1
    if t == fail:
        result = -1
    if success >= 1:
        result = t
    return result 
"""
