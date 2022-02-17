from typing import List


def binary_search(nums: List[int], target: int) -> int:
    low = 0
    high = len(nums) - 1
    while low <= high:
        mid = (low + high) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1


def two_sum(nums: List[int], target: int) -> List[int]:
    for i in range(len(nums)):  # First traversal loop
        # Use a binary search to reduce time complexity
        match = target - nums[i]
        other_index = binary_search(nums, match)
        if (other_index != -1):
            return [i, other_index]

    return None
