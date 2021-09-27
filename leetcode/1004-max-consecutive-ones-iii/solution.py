# https://leetcode.com/problems/max-consecutive-ones-iii/

from typing import List


class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        tmp = {1: 0, 0: 0}
        start, longest = 0, 0
        for end in range(len(nums)):
            tmp[nums[end]] += 1

            while end - start + 1 - tmp[1] > k:
                tmp[nums[start]] -= 1
                start += 1

            longest = max(longest, end - start + 1)
        return longest


if __name__ == "__main__":
    print(Solution().longestOnes([1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0], 2))  # 6
    print(Solution().longestOnes(
        [0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1, 1], 3))  # 9
    print(Solution().longestOnes(
        [0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1], 3))  # 10
    print(Solution().longestOnes([0, 0, 0, 0], 0))  # 0
