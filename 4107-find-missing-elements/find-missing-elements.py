from typing import List

class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        missing = []

        start = min(nums)
        end = max(nums)

        for num in range(start, end + 1):
            if num not in nums:
                missing.append(num)

        return missing        