from typing import List


class AverageOfSubarrayOfSizeK:
    # Time complexity: O(N * K)
    def findAveragesBruteForce(self, k: int, arr: List[int]) -> List[float]:
        result = []
        for i in range(len(arr) - k + 1): # number of subarray  = n - k + 1
            _sum = 0
            for j in range(i, i + k):
                _sum += arr[j]
            result.append(_sum / k)
        return result

    # Time complexity: O(N)
    def findAverages(self, k: int, arr: List[int]) -> List[float]:
        result = []
        _sum = 0
        for i in range(len(arr)):
            _sum += arr[i]
            if i >= k - 1:
                result.append(_sum / k)
                _sum -= arr[i - k + 1]

        return result


if __name__ == "__main__":
    print(AverageOfSubarrayOfSizeK().findAverages(
        5, [1, 3, 2, 6, -1, 4, 1, 8, 2]))
    print(AverageOfSubarrayOfSizeK().findAveragesBruteForce(
        5, [1, 3, 2, 6, -1, 4, 1, 8, 2]))
