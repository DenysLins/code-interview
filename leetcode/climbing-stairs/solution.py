class Solution:
    def climbStairs(self, n: int) -> int:
        self.n = n
        a, b = 1, 2
        if n < 2:
            return n
        else:
            for i in range(3, n + 1):
                a, b = b, a + b
            return b


if __name__ == "__main__":
    print(Solution().climbStairs(10))
