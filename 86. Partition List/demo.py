# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        GreaterHead = GreaterTail = ListNode()
        LessHead = LessTail = ListNode()
        while head:
            if head.val < x:
                LessTail.next = head
                LessTail = LessTail.next
            else:
                GreaterTail.next = head
                GreaterTail = GreaterTail.next
            
            head = head.next
        print(GreaterTail.next.val, GreaterTail.next.val, GreaterTail.next.next)

        GreaterTail.next = None
        LessTail.next = GreaterHead.next
        return LessHead.next


def convert_array2ListNode(arr):
    head = None
    for v in arr[::-1]:
        head = ListNode(val=v ,next=head)
        
    return head

def convert_ListNode2array(head):
    cnt = 0
    arr = []
    while head and cnt<20:
        arr.append(head.val)
        head = head.next
        cnt += 1
    return arr

if __name__ == "__main__":
    head = [1,4,3,2,5,2]
    x = 3

    # head = [2,1]
    # x = 2

    ans = convert_array2ListNode(head)

    sl = Solution()
    ans = sl.partition(ans, x)

    ans = convert_ListNode2array(ans)
    print(ans)