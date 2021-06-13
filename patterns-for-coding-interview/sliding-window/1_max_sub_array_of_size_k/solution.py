# Time Complexity O(N). Space Complexity O(1)
from typing import List


def findMaxSumSubarray(k: int, arr: List[int]) -> int:
    _sum = 0
    _max = 0
    for i in range(len(arr)):
        _sum += arr[i]
        if (i >= k - 1):
            _max = max(_max, _sum)
            _sum -= arr[i - k + 1]
    return _max


print(findMaxSumSubarray(3, [2, 1, 5, 1, 3, 2]))
print(findMaxSumSubarray(2, [2, 3, 4, 1, 5]))
