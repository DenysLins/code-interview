# https://leetcode.com/problems/longest-substring-without-repeating-characters/


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
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


if __name__ == "__main__":
    print(Solution().lengthOfLongestSubstring("abcabcbb"))
    print(Solution().lengthOfLongestSubstring("bbbbb"))
    print(Solution().lengthOfLongestSubstring("pwwkew"))
    print(Solution().lengthOfLongestSubstring(""))
    print(Solution().lengthOfLongestSubstring("dvdf"))
