import typing as tp
from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        newHead  = ListNode(val=None)
        newHead.next = head
        CN :ListNode = newHead
        FN : ListNode = newHead.next

        while FN and FN.next:
            if FN.val != FN.next.val:
                CN.next = FN
                CN, FN = CN.next, FN.next
            elif (FN.next.next is None) or (FN.next.val != FN.next.next.val):
                FN = FN.next.next
            else:
                FN = FN.next

        CN.next = FN

        return newHead.next



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
    head = [1,2,3,3,4,4,5]
    head = [1,1,1,2,3]
    head = [1,2,3,3,4,4]
    head = [1,1,1,1,1]
    head = [1,1,1,2]
    head = [0,1,2,2,3,4]

    ans = Solution.conv_arr2LN(head)

    sl = Solution()
    ans = sl.deleteDuplicates(head=ans)

    ans = Solution.conv_LN2arr(ans)
    print(ans)
        