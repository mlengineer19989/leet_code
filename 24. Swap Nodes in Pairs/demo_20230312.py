import typing as tp
from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        newHead = dummyHead =ListNode()
        dummyHead.next = head

        while dummyHead.next and dummyHead.next.next:
            N1 :ListNode = dummyHead.next
            N2 :ListNode = N1.next
            N3 :ListNode = N2.next

            dummyHead.next = N2
            dummyHead.next.next = N1
            dummyHead.next.next.next = N3

            dummyHead = dummyHead.next.next

        return newHead.next

    @staticmethod
    def conv_arr2ListNode(arr : tp.List[int]) -> ListNode:
        LN : ListNode = None
        for v in arr[::-1]:
            LN = ListNode(val=v, next=LN)
        return LN

    @staticmethod
    def conv_ListNode2arr(LN : ListNode) -> tp.List[int]:
        arr = []
        while LN:
            arr.append(LN.val)
            LN = LN.next
        return arr
    
if __name__ == "__main__":
    head = [1,2,3,4]
    head = []
    head = [1]
    head = [1, 2, 3]

    head = Solution.conv_arr2ListNode(head)

    sl = Solution()
    ans = sl.swapPairs(head=head)

    ans = Solution.conv_ListNode2arr(ans)
    print(ans)