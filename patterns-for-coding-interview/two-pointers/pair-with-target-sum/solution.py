from typing import List


class PairWithTargetSum:
    def search(self, arr: List[int], targetSum: int) -> List[int]:
        i, j = 0, len(arr) - 1
        result = [-1, -1]
        for n in range(len(arr)):
            sum = arr[i] + arr[j]
            if sum > targetSum:
                j -= 1
            elif sum < targetSum:
                i += 1
            else:
                return [i, j]
        return result


if __name__ == "__main__":
    print(PairWithTargetSum().search([1, 2, 3, 4, 6], 6))
    print(PairWithTargetSum().search([2, 5, 9, 11], 11))
    print(PairWithTargetSum().search([2, 5, 9, 11], 1))
