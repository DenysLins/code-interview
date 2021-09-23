# https://leetcode.com/problems/rotate-array/

from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        begin = len(nums) - 1
        length = len(nums)

        if k == 0 or k % length == 0:
            pass
        else:
            for i in range(k-1):
                begin -= 1
                if begin < 0:
                    begin = len(nums) - 1
            begin % length
            nums[:] = nums[begin:] + nums[:begin]

        print(nums)


if __name__ == "__main__":
    print(Solution().rotate([1, 2, 3, 4, 5, 6, 7], 1))
