# Time Complexity O(N**2). Space Complexity O(N)

from typing import List


class Solution:
    def searchTriplets(self, nums: List[int]) -> List[int]:
        result = []
        nums.sort()
        for i in range(len(nums) - 2):
            j = i + 1
            k = len(nums) - 1
            while j < k:
                if i != j and i != k and j != k and nums[i] + nums[j] + nums[k] == 0 and [nums[i], nums[j], nums[k]] not in result:
                    result.append([nums[i], nums[j], nums[k]])
                if nums[i] + nums[j] + nums[k] > 0:
                    k -= 1
                else:
                    j += 1

        return result


if __name__ == "__main__":
    print(Solution().searchTriplets([-3, 0, 1, 2, -1, 1, -2]))
    print(Solution().searchTriplets([-5, 2, -1, -2, 3]))
    print(Solution().searchTriplets([0, 0, 0]))
