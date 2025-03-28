

### Brute Force Approach ###

# def twoSum(nums, target):
#     for i in range(len(nums)):
#         for j in range(i+1, len(nums)):
#             if nums[i] + nums[j] == target:
#                 return [i, j]
#     return None


### Optimized Approach ###

def twoSum(nums, target):
    num_to_index = {}
    for i, num in enumerate(nums):
        if target - num in num_to_index:
            return [num_to_index[target - num], i]
        num_to_index[num] = i
    return None


# Example usage
if __name__ == "__main__":
    nums = [2, 7, 11, 15]
    target = 9
    print(twoSum(nums, target))  # Output: [0, 1]
    nums = [3, 2, 4]
    target = 6
    print(twoSum(nums, target))  # Output: [1, 2]
    nums = [3, 3]
    target = 6
    print(twoSum(nums, target))  # Output: [0, 1]
    nums = [3, 2, 3]
    target = 6
    print(twoSum(nums, target))  # Output: [0, 2]
    nums = [3, 2, 4]
    target = 8
    print(twoSum(nums, target))  # Output: None
    nums = [3, 2, 4]
    target = 5
    print(twoSum(nums, target))  # Output: None
    nums = [3, 2, 4]
    target = 4
    print(twoSum(nums, target))  # Output: None
    nums = [3, 2, 4]
    target = 7
    print(twoSum(nums, target))  # Output: [1, 2]
    nums = [3, 2, 4]
    target = 3
    print(twoSum(nums, target))  # Output: None
    nums = [3, 2, 4]
    target = 2
    print(twoSum(nums, target))  # Output: None
    nums = [3, 2, 4]
    target = 1
    print(twoSum(nums, target))  # Output: None
    nums = [3, 2, 4]
    target = 0
    print(twoSum(nums, target))  # Output: None
    nums = [3, 2, 4]
    target = -1
    print(twoSum(nums, target))  # Output: None
    nums = [3, 2, 4]
    target = -2
    print(twoSum(nums, target))  # Output: None
    nums = [3, 2, 4]