# https://leetcode.com/problems/search-insert-position/

from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        start, end = 0, len(nums)
        while start != end:
            middle = (start + end) // 2
            if nums[middle] == target:
                return middle
            if target > nums[middle]:
                start = middle + 1
            else:
                end = middle
        return start


if __name__ == "__main__":
    print(Solution().searchInsert([1, 3, 5, 6], 5))
    print(Solution().searchInsert([1, 3, 5, 6], 2))
    print(Solution().searchInsert([1, 3, 5, 6], 7))
    print(Solution().searchInsert([1, 3, 5, 6], 0))
    print(Solution().searchInsert([1], 0))
