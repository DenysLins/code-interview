# Time Complexity O(N). Space Complexity O(1)
from typing import List


class MaxSumSubarrayOfSizeK:
    def findMaxSumSubarray(self, k: int, arr: List[int]) -> int:
        _sum = 0
        _max = 0
        for i in range(len(arr)):
            _sum += arr[i]
            if (i >= k - 1):
                _max = max(_max, _sum)
                _sum -= arr[i - k + 1]
        return _max


if __name__ == "__main__":
    print(MaxSumSubarrayOfSizeK().findMaxSumSubarray(3, [2, 1, 5, 1, 3, 2]))
    print(MaxSumSubarrayOfSizeK().findMaxSumSubarray(2, [2, 3, 4, 1, 5]))
