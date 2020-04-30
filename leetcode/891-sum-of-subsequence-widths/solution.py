# https://leetcode.com/problems/sum-of-subsequence-widths/

from typing import List


class Solution:
    def sumSubseqWidths(self, A: List[int]) -> int:
        A.sort()
        total = 0
        n = len(A)

        for i, num in enumerate(A):
            total += (1 << i) * num
            total -= (1 << (n - 1 - i)) * num

        return total % (10**9 + 7)


if __name__ == "__main__":
    print(Solution().sumSubseqWidths([2, 1, 3]))
