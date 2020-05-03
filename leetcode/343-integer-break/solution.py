# https://leetcode.com/problems/integer-break/


class Solution:
    def integerBreak(self, n: int) -> int:

        if n <= 3:
            return n - 1

        r = n % 3

        if r == 0:
            return 3**(n // 3)
        elif r == 1:
            return 3**(n // 3 - 1) * 4
        else:
            return 3**(n // 3) * r


if __name__ == "__main__":
    print(Solution().integerBreak(14))
