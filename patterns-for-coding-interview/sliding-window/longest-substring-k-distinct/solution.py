
class LongestSubstringKDistinct:
    # Time complexity = O(S). Space complexity = O(K)
    def findLength(self, s: str, k: int ) -> int:
        longest = 0
        start = 0
        chars = {}
        for i, c in enumerate(s):
            if c not in chars:
                chars[c] = 1
            else:
                chars[c] = chars.get(c) + 1
            while len(chars.keys()) > k:
                cs = s[start]
                chars[cs] = chars.get(cs) - 1
                if chars[cs] == 0:
                    chars.pop(cs)
                start += 1
            longest = max(i - start + 1, longest)
        return longest



if __name__ == "__main__":
    print(LongestSubstringKDistinct().findLength("araaci", 2))
    print(LongestSubstringKDistinct().findLength("araac1", 1))
    print(LongestSubstringKDistinct().findLength("cbbedbi", 3))
