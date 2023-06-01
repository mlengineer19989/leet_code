from typing import Optional, List

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummyHead = ListNode()
        dummyHead.next = head
        left = right = dummyHead

        for i in range(n):
            right =right.next

        while right.next is not None:
            left = left.next
            right = right.next

        left.next = left.next.next

        return dummyHead.next
    

    @staticmethod
    def conv_arr2List(arr:List[int]) -> Optional[ListNode]:
        dummy = head = ListNode()
        for v in arr:
            head.next = ListNode(val=v, next=None)
            head = head.next
        return dummy.next
    
    @staticmethod
    def conv_List2arr(head:Optional[ListNode]) -> List[int]:
        arr:List[int] = []

        while head is not None:
            arr.append(head.val)
            head = head.next
        return arr
    
if __name__ == "__main__":
    head = [1,2,3,4,5]
    n = 2

    head = [1]
    n = 1

    head = [1,2]
    n = 1

    head = Solution.conv_arr2List(head)

    sl = Solution()
    ans = sl.removeNthFromEnd(head, n)

    ans = Solution.conv_List2arr(ans)
    print(ans)