# Time Complexity O(N). Space Complexity O(1)

from typing import List


class RemoveDuplicates:
    def remove(self, arr: List[int]) -> int:
        count = 0
        for i in range(1, len(arr)):
            if arr[i - 1] == arr[i]:
                count += 1
        return len(arr) - count


if __name__ == "__main__":
    print(RemoveDuplicates().remove([2, 3, 3, 3, 6, 9, 9]))
    print(RemoveDuplicates().remove([2, 2, 2, 11]))
    print(RemoveDuplicates().remove([1, 2, 3]))
    print(RemoveDuplicates().remove([1, 1, 1]))
