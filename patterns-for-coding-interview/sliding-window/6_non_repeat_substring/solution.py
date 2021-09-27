# https://leetcode.com/problems/longest-substring-without-repeating-characters/
# Time complexity = O(N). Space complexity = O(1)


def non_repeat_substring(s: str) -> int:
    tmp = {}
    start, end, longest = 0, 0, 0
    for i in s:
        if i not in tmp:
            tmp[i] = 1
            longest = max(longest, end - start + 1)
        else:
            tmp[i] += 1
            while max(tmp.values()) > 1:
                if tmp[s[start]] > 1:
                    tmp[s[start]] -= 1
                else:
                    tmp.pop(s[start])
                start += 1
        end += 1

    return longest


print(non_repeat_substring("abcabcbb"))
print(non_repeat_substring("bbbbb"))
print(non_repeat_substring("pwwkew"))
print(non_repeat_substring(""))
print(non_repeat_substring("dvdf"))
