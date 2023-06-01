# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        slow = fast = ListNode()
        fast.next = head
        newHead = slow
        for i in range(n):
            fast = fast.next

        while fast.next:
            slow = slow.next
            fast = fast.next
        slow.next = slow.next.next
        return newHead.next
    
def conv_arr2ListNode(arr : list):
    LN = None
    for v in arr[::-1]:
        LN = ListNode(val=v, next=LN)
    return LN

def conv_ListNode2arr(LN : ListNode):
    arr = []
    while LN:
        arr.append(LN.val)
        LN = LN.next
    return arr

if __name__ == "__main__":
    # head = [1,2,3,4,5]
    # n = 2

    # head = [1]
    # n = 1

    # head = [1,2]
    # n = 1

    # head = [1,2]
    # n = 2

    head = [1,2,3]
    n = 3
    
    head = conv_arr2ListNode(head)

    sl = Solution()
    head = sl.removeNthFromEnd(head=head, n=n)

    ans = conv_ListNode2arr(head)
    print(ans)