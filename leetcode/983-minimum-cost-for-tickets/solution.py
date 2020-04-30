# https://leetcode.com/problems/minimum-cost-for-tickets/

from typing import List


class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        # Get the biggest day
        n = days[-1]

        # Creates an array with zeros for index not in days and 1 for index in days
        dp = [1 if x in days else 0 for x in range(n + 1)]

        for j in range(1, n + 1):

            # if the actual value is 0, copy the value from the previous position
            if dp[j] == 0:
                dp[j] = dp[j - 1]

            # if the actual value is 1, calculate three values:
            # x is the value stored in index - 1, plus the daily cost
            # y is the value stored in index - 7, plus the weekly cost
            # z is the value stored in index - 30, plus the monthly cost
            # get the minimum between x,y,z and store in the actual position
            else:
                x = dp[max(j - 1, 0)] + costs[0]
                y = dp[max(j - 7, 0)] + costs[1]
                z = dp[max(j - 30, 0)] + costs[2]
                dp[j] = min(x, y, z)

        return dp[n]


if __name__ == "__main__":
    print(Solution().mincostTickets([1, 4, 6, 7, 8, 20], [2, 7, 15]))
