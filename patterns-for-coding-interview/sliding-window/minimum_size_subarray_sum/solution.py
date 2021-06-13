from typing import List
import sys


def findMinSubarray(s: int, arr: List[int]) -> int:
    # Time Complexity O(N). Space Complexity O(1)
    _sum = 0
    _start = 0
    _min = sys.maxsize
    for i in range(len(arr)):
        _sum += arr[i]
        while _sum >= s:
            _min = min(i - _start + 1, _min)
            _sum -= arr[_start]
            _start += 1

    return 0 if _min == sys.maxsize else _min


print(findMinSubarray(7, [2, 1, 5, 2, 3, 2]))
print(findMinSubarray(7, [2, 1, 5, 2, 8]))
print(findMinSubarray(8, [3, 4, 1, 1, 6]))
print(findMinSubarray(25, [3, 4, 2, 5, 6]))
