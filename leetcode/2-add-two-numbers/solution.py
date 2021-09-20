# https://leetcode.com/problems/add-two-numbers/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        result = []
        carry = 0

        while l1 or l2:
            v1, v2 = 0, 0
            if l1:
                v1 = l1.val
                l1 = l1.next
            if l2:
                v2 = l2.val
                l2 = l2.next
            s = (v1 + v2 + carry) % 10
            carry = (v1 + v2 + carry) // 10
            result.append(ListNode(s))
            if(len(result) > 1):
                result[-2].next = result[-1]

        if carry != 0:
            result.append(ListNode(carry))
            if(len(result) > 1):
                result[-2].next = result[-1]

        return result[0]


n3l1 = ListNode(9)
n2l1 = ListNode(9, n3l1)
n1l1 = ListNode(9, n2l1)
n0l1 = ListNode(9, n1l1)

# n6l2 = ListNode(9)
# n5l2 = ListNode(9, n6l2)
# n4l2 = ListNode(9, n5l2)
n3l2 = ListNode(9)
n2l2 = ListNode(9, n3l2)
n1l2 = ListNode(9, n2l2)
n0l2 = ListNode(9, n1l2)

if __name__ == "__main__":
    print(Solution().addTwoNumbers(n0l1, n0l2))

#   1 1 1 1 1 1 1
# 9 9 9 9 9 9 9
# 9 9 9 9
# 8 9 9 9 0 0 0 1
