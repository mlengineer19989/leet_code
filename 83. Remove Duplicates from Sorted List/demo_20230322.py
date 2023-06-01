import typing as tp
from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return head
        
        dummyHead = newHead = ListNode(val=None)
        dummyHead.next = head

        while dummyHead and dummyHead.next:
            if dummyHead.val == dummyHead.next.val:
                dummyHead.next = dummyHead.next.next
            else:
                dummyHead = dummyHead.next
        return newHead.next

    @staticmethod
    def conv_arr2LN(arr : tp.List[int]):
        LN : ListNode = None
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
    head = [1,1,1,2,3,3]
    head = [1,1,2,2,2,4,4,4,4,4]
    head = [0,0,0,0,0]

    ans = Solution.conv_arr2LN(head)

    sl = Solution()
    ans = sl.deleteDuplicates(ans)

    ans = Solution.conv_LN2arr(ans)
    print(ans)
