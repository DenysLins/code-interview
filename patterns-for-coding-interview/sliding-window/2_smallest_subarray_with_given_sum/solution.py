# Time Complexity O(N). Space Complexity O(1)
import sys


def smallest_subarray_with_given_sum(s, arr):
    _sum = 0
    _window_start = 0
    _window_end = 0
    _min_len = sys.maxsize
    for i in range(len(arr)):
        _sum += arr[i]
        _window_end += 1
        while _sum >= s:
            if _window_end - _window_start < _min_len:
                _min_len = _window_end - _window_start
            _sum -= arr[_window_start]
            _window_start += 1
    if _min_len == sys.maxsize:
      _min_len = 0

    return _min_len


print("Smallest subarray length: {}".format(
    smallest_subarray_with_given_sum(7, [2, 1, 5, 2, 3, 2])))
print("Smallest subarray length: {}".format(
    smallest_subarray_with_given_sum(7, [2, 1, 5, 2, 8])))
print("Smallest subarray length: {}".format(
    smallest_subarray_with_given_sum(8, [2, 1, 5, 2, 3, 2])))
print("Smallest subarray length: {}".format(
    smallest_subarray_with_given_sum(200, [2, 1, 5, 2, 3, 2])))
