# https://leetcode.com/problems/longest-substring-without-repeating-characters/
# Time complexity = O(N). Space complexity = O(1)


from typing import List


def length_of_longest_substring(nums: List[int], k: int) -> int:
    tmp = {1: 0, 0: 0}
    start, longest = 0, 0
    for end in range(len(nums)):
        tmp[nums[end]] += 1

        while end - start + 1 - tmp[1] > k:
            tmp[nums[start]] -= 1
            start += 1

        longest = max(longest, end - start + 1)
    return longest


print(length_of_longest_substring([1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0], 2))  # 6
print(length_of_longest_substring(
    [0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1, 1], 3))  # 9
print(length_of_longest_substring(
    [0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1], 3))  # 10
print(length_of_longest_substring([0, 0, 0, 0], 0))  # 0
