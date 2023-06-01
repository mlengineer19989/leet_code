import typing as tp
from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        N : ListNode = head
        length : int = 0
        while N:
            N = N.next
            length += 1

        if length==0:
            return head

        k : int = k%length

        dummyHead = ListNode()
        dummyHead.next = head
        N = dummyHead.next

        while N.next:
            N = N.next
        N.next = dummyHead.next

        for i in range(length - k + 1):
            dummyHead = dummyHead.next
        N = dummyHead

        for i in range(length-1):
            N = N.next
        N.next = None

        return dummyHead

    @staticmethod
    def conv_arr2LN(arr : tp.List[int]):
        LN = None
        for v in arr[::-1]:
            LN = ListNode(val=v, next=LN)
        return LN
    
    @staticmethod
    def conv_LN2arr(LN : ListNode):
        arr : tp.List[int] = []
        while LN:
            arr.append(LN.val)
            LN = LN.next
        return arr
    
if __name__ == "__main__":
    head = [1,2,3,4,5]
    k = 2

    head = [0,1,2]
    k = 4

    head = []
    k = 0

    ans = Solution.conv_arr2LN(head)

    sl = Solution()
    ans = sl.rotateRight(head=ans, k=k)

    ans = Solution.conv_LN2arr(ans)
    print(ans)