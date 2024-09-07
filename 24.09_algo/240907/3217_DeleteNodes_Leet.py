# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        # 리스트 노드의 값을 문자열로 출력
        result = []
        current = self
        while current:
            result.append(str(current.val))
            current = current.next
        return " -> ".join(result)

from typing import List,Optional


class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        snum = set(nums)
        dummy = ListNode(0)
        current = dummy

        while head:
            if head.val not in snum:
                current.next = ListNode(head.val)
                current = current.next
            head = head.next
        # print(dummy.next)
        return dummy.next

s = Solution()
s.modifiedList(
nums = [1,2,3], head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, None)))))
)