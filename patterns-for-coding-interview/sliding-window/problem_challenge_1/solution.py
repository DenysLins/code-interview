# https://leetcode.com/problems/permutation-in-string/
# Time complexity = O(N + M). Space complexity = O(M)


from typing import List


def findPermutation(str: str, pattern: str) -> bool:
    pattern_dict = {}
    start = 0
    for i in pattern:
        if i not in pattern_dict:
            pattern_dict[i] = 0
        pattern_dict[i] += 1

    for end in range(len(str)):
        right = str[end]
        if right in pattern_dict:
            pattern_dict[right] -= 1

        # if all(x == 0 for x in pattern_dict.values()):
        if not any(pattern_dict.values()):
            return True

        if end >= len(pattern) - 1:
            left = str[start]
            start += 1
            if left in pattern_dict:
                pattern_dict[left] += 1

    return False


print(findPermutation("aaacb", "abc"))  # true
print(findPermutation("odicf", "dc"))  # false
print(findPermutation("bcdxabcdy", "bcdyabcdx"))  # true
print(findPermutation("aaacb", "abc"))  # true
