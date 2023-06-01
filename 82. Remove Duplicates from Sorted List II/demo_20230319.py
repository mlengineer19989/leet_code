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

        newHead = dummyHead = ListNode()
        LN1 : ListNode = ListNode(val=None, next=head)
        LN2 : ListNode = LN1.next
        LN3 : ListNode = LN2.next

        while LN3 and LN3.next:
            if LN2.val == LN3.val:
                LN1, LN2, LN3 = LN1.next.next, LN2.next.next, LN3.next.next
            else:
                if LN1.val != LN2.val:
                    dummyHead.next = ListNode(val=LN2.val)
                    dummyHead = dummyHead.next
                LN1, LN2, LN3 = LN1.next, LN2.next, LN3.next
        if LN3:
            if LN2.val != LN3.val:
                if (LN1.val != LN2.val):
                    dummyHead.next = ListNode(val=LN2.val)
                    dummyHead = dummyHead.next
                dummyHead.next = ListNode(val=LN3.val)
        else:
            if LN1.val != LN2.val:
                dummyHead.next = ListNode(val=LN2.val)
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
    #head = [1,1,1,2,3]
    #head = [1,2,3,3,4,4]
    #head = [1,1,1,1,1]
    #head = [1,1,1,2]
    head = [0,1,2,2,3,4]

    ans = Solution.conv_arr2LN(head)

    sl = Solution()
    ans = sl.deleteDuplicates(head=ans)

    ans = Solution.conv_LN2arr(ans)
    print(ans)
        