# https://leetcode.com/problems/permutation-in-string/

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        pattern_dict = {}
        start = 0
        for i in s1:
            if i not in pattern_dict:
                pattern_dict[i] = 0
            pattern_dict[i] += 1

        for end in range(len(s2)):
            right = s2[end]
            if right in pattern_dict:
                pattern_dict[right] -= 1

            if len(set(pattern_dict.values())) == 1 and set(pattern_dict.values()).pop() == 0:
                return True

            if end >= len(s1) - 1:
                left = s2[start]
                start += 1
                if left in pattern_dict:
                    pattern_dict[left] += 1

        return False


if __name__ == "__main__":
    print(Solution().checkInclusion("abc", "aaacb"))  # True
    print(Solution().checkInclusion("dc", "odicf"))  # False
    print(Solution().checkInclusion("bcdyabcdx", "bcdxabcdy"))  # True
    print(Solution().checkInclusion("abc", "aaacb"))  # True
