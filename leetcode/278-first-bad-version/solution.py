# https://leetcode.com/problems/first-bad-version/

# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):

# 0  1  2  3  4  5  6  7  8  9
# 1  2  3  4  5  6  7  8  9  10
# 0  0  0  0  x  x  x  x  x  x

class Solution:
    def firstBadVersion(self, n):
        start = 0
        end = n - 1
        while start != end:
            middle = (start + end) // 2
            if not self.isBadVersion(middle + 1):
                start = middle + 1
            else:
                end = middle
        return start + 1

    def isBadVersion(self, n):
        return n >= 4


if __name__ == "__main__":
    print(Solution().firstBadVersion(5))
