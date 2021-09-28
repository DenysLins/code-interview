# Time Complexity O(N). Space Complexity O(N)

from typing import List


class PairWithTargetSum:
    def search(self, arr: List[int], targetSum: int) -> List[int]:
        left, right = 0, len(arr) - 1
        result = [-1, -1]
        while left < right:
            sum = arr[left] + arr[right]
            if sum > targetSum:
                right -= 1
            elif sum < targetSum:
                left += 1
            else:
                return [left, right]
        return result


if __name__ == "__main__":
    print(PairWithTargetSum().search([1, 2, 3, 4, 6], 6))
    print(PairWithTargetSum().search([2, 5, 9, 11], 11))
    print(PairWithTargetSum().search([2, 5, 9, 11], 1))
