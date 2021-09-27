# https://leetcode.com/problems/longest-substring-without-repeating-characters/
# Time complexity = O(N). Space complexity = O(1)


def length_of_longest_substring(s: str, k: int) -> int:
    tmp = {}
    start, longest = 0, 0
    for end in range(len(s)):
        if s[end] not in tmp:
            tmp[s[end]] = 0
        tmp[s[end]] += 1

        while end - start + 1 - max(tmp.values()) > k:
            tmp[s[start]] -= 1
            start += 1

        longest = max(longest, end - start + 1)
    return longest


print(length_of_longest_substring("ABAB", 2))  # 4
print(length_of_longest_substring("AABABBA", 1))  # 4
print(length_of_longest_substring("aabccbb", 2))  # 5
print(length_of_longest_substring("", 0))  # 0
print(length_of_longest_substring("ABBB", 2))  # 4
