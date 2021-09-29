# Time Complexity O(N**2). Space Complexity O(N)

from typing import List
import sys


class Solution:
    def searchTriplets(self, nums: List[int], target: int) -> int:
        difference = 1000000
        result = 0
        nums.sort()
        for i in range(len(nums) - 1):
            j = i + 1
            k = len(nums) - 1
            while j < k:
                sum = nums[i] + nums[j] + nums[k]
                if abs(sum - target) < difference:
                    difference = abs(
                        sum - target)
                    result = sum
                if sum - target > 0:
                    k -= 1
                else:
                    j += 1

        return result


if __name__ == "__main__":
    print(Solution().searchTriplets([-2, 0, 1, 2], 2))  # 1
    print(Solution().searchTriplets([-3, -1, 1, 2], 1))  # 0
    print(Solution().searchTriplets([1, 0, 1, 1], 100))  # 3
    print(Solution().searchTriplets([-1, 2, 1, -4], 1))  # 2
    print(Solution().searchTriplets([0, 0, 0], 1))  # 0