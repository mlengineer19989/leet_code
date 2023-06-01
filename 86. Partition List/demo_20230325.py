import typing as tp
from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        LHead = LTail = ListNode()
        GHead = GTail = ListNode()
        
        while head:
            if head.val < x:
                LTail.next = head
                LTail = LTail.next
            else:
                GTail.next = head
                GTail = GTail.next
            head = head.next
        GTail.next = None
        LTail.next = GHead.next
        return LHead.next

    @staticmethod
    def conv_arr2LN(arr:tp.List[int]) -> ListNode:
        LN:ListNode = None
        for v in arr[::-1]:
            LN = ListNode(val=v, next=LN)
        return LN
    
    @staticmethod
    def conv_LN2arr(LN:ListNode) -> tp.List[int]:
        arr:tp.List[int] = []
        while LN:
            arr.append(LN.val)
            LN = LN.next
        return arr
    

if __name__ == "__main__":
    head = [1,4,3,2,5,2]
    x = 3

    head = [2,1]
    x = 2

    ans = Solution.conv_arr2LN(head)

    sl = Solution()
    ans = sl.partition(head=ans, x=x)

    ans = Solution.conv_LN2arr(ans)
    print(ans)