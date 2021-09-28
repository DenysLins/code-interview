# https://leetcode.com/problems/find-all-anagrams-in-a-string/]

from typing import List


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        pattern_dict = {}
        start = 0
        result = []
        for i in p:
            if i not in pattern_dict:
                pattern_dict[i] = 0
            pattern_dict[i] += 1

        for end in range(len(s)):
            right = s[end]
            if right in pattern_dict:
                pattern_dict[right] -= 1

            # if all(x == 0 for x in pattern_dict.values()):
            if not any(pattern_dict.values()):
                result.append(start)

            if end >= len(p) - 1:
                left = s[start]
                start += 1
                if left in pattern_dict:
                    pattern_dict[left] += 1

        return result


print(Solution().findAnagrams("ppqp", "pq"))  # [1, 2]
print(Solution().findAnagrams("abbcabc", "abc"))  # [2, 3, 4]
print(Solution().findAnagrams("cbaebabacd", "abc"))  # [0, 6]
print(Solution().findAnagrams("abab", "ab"))  # [0, 1, 2]
