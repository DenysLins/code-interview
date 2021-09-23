# https://leetcode.com/problems/longest-repeating-character-replacement/


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
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


if __name__ == "__main__":
    print(Solution().characterReplacement("ABAB", 2))  # 4
    print(Solution().characterReplacement("AABABBA", 1))  # 4
    print(Solution().characterReplacement("aabccbb", 2))  # 5
    print(Solution().characterReplacement("", 0))  # 5
    print(Solution().characterReplacement("ABBB", 2))  # 4
