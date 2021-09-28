# Time Complexity O(N). Space Complexity O(N)

from typing import List


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        i = 0
        j = len(nums) - 1
        result = []
        while i <= j:
            t1 = nums[i] ** 2
            t2 = nums[j] ** 2
            if t1 < t2:
                result.insert(0, t2)
                j -= 1
            else:
                result.insert(0, t1)
                i += 1

        return result


if __name__ == "__main__":
    print(Solution().sortedSquares([-4, -1, 0, 3, 10]))
    print(Solution().sortedSquares([-7, -3, 2, 3, 11]))
