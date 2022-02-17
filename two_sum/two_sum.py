from typing import List


def two_sum(nums: List[int], target: int) -> List[int]:
    # Find the 1st index in the list
    for i in range(len(nums)):
        # find the other index starting at i+1
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]
    return None
