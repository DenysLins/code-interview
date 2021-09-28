# Time Complexity O(N**2). Space Complexity O(N)

from typing import List


class Solution:
    def searchTriplets(self, nums: List[int]) -> List[int]:
        result = []
        nums.sort()
        for i in range(len(nums) - 1):
            j = i + 1
            k = len(nums) - 1
            target = -nums[i]
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            while j <= k:
                if nums[j] + nums[k] == target and [-target, nums[j], nums[k]] not in result:
                    result.append([-target, nums[j], nums[k]])
                if nums[j] + nums[k] > target:
                    k -= 1
                else:
                    j += 1

        return result


if __name__ == "__main__":
    print(Solution().searchTriplets([-3, 0, 1, 2, -1, 1, -2]))
    print(Solution().searchTriplets([-5, 2, -1, -2, 3]))
