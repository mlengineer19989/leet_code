from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummyHead = newHead = ListNode()

        while list1 and list2:
            if list1.val <= list2.val:
                dummyHead.next = list1
                list1 = list1.next
            else:
                dummyHead.next = list2
                list2 = list2.next

            dummyHead = dummyHead.next

        if list1:
            dummyHead.next = list1
        elif list2:
            dummyHead.next =list2

        return newHead.next
    
    @staticmethod
    def convert_arr2LN(arr:list[int]) -> ListNode:
        LN:ListNode = None
        for v in arr[::-1]:
            LN = ListNode(val=v, next=LN)
        return LN
    
    @staticmethod
    def convert_LN2arr(LN:ListNode) -> list[int]:
        arr:list[int] = []
        while LN:
            arr.append(LN.val)
            LN = LN.next
        return arr
    
if __name__ == "__main__":
    list1 = [1,2,4]
    list2 = [1,3,4]

    list1 = []
    list2 = []

    list1 = []
    list2 = [0]

    LN1 = Solution.convert_arr2LN(list1)
    LN2 = Solution.convert_arr2LN(list2)

    sl = Solution()
    ans = sl.mergeTwoLists(list1=LN1, list2=LN2)

    print(Solution.convert_LN2arr(ans))