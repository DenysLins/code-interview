# https://leetcode.com/problems/fruit-into-baskets/
# Time complexity = O(N). Space complexity = O(1)


from typing import List


def totalFruit(fruits: List[int]) -> int:
    start = end = longest = 0
    tmp = {}
    for i in fruits:
        if i not in tmp:
            tmp[i] = 1
            while len(tmp.keys()) > 2:
                if tmp[fruits[start]] > 1:
                    tmp[fruits[start]] -= 1
                else:
                    tmp.pop(fruits[start])
                start += 1
        else:
            tmp[i] += 1
        longest = max(longest, end - start + 1)
        end += 1

    return longest


print(totalFruit([]))  # 0
print(totalFruit([1]))  # 1
print(totalFruit([1, 2, 1]))  # 3
print(totalFruit([0, 1, 2, 2]))  # 3
print(totalFruit([1, 2, 3, 2, 2]))  # 4
print(totalFruit([3, 3, 3, 1, 2, 1, 1, 2, 3, 3, 4]))  # 5
print(totalFruit(['A', 'B', 'C', 'B', 'B', 'C']))  # 5
print(totalFruit(['A', 'B', 'C', 'A', 'C']))  # 3
