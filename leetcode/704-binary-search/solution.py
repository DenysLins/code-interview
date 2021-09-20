# https://leetcode.com/problems/binary-search/

from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start = 0
        end = len(nums)
        while start != end:
            middle = (start + end) // 2
            if nums[middle] == target:
                return middle
            elif target > nums[middle]:
                start = middle + 1
            else:
                end = middle
        return -1


if __name__ == "__main__":
    print(Solution().search([-1, 0, 3, 5, 9, 12], -1))
    print(Solution().search([-1, 0, 3, 5, 9, 12], 0))
    print(Solution().search([-1, 0, 3, 5, 9, 12], 3))
    print(Solution().search([-1, 0, 3, 5, 9, 12], 5))
    print(Solution().search([-1, 0, 3, 5, 9, 12], 9))
    print(Solution().search([-1, 0, 3, 5, 9, 12], 12))
    print(Solution().search([-1, 0, 3, 5, 9, 12], 2))
