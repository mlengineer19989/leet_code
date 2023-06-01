# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if head is None:
            return head

        newHead = dummyHead = ListNode()
        dummyHead.next = head
        dummyHead = dummyHead.next

        while dummyHead.next:
            if dummyHead.val == dummyHead.next.val:
                dummyHead.next = dummyHead.next.next
            else:
                dummyHead = dummyHead.next
        return newHead.next

def convert_array2ListNode(arr):
    head = None
    for v in arr[::-1]:
        head = ListNode(val=v, next=head)
    return head

def convert_ListNode2array(head):
    arr = []
    while head:
        arr.append(head.val)
        head = head.next
    return arr

if __name__ == "__main__":
    head = [1,1,2,3,3]
    head = [1,1,2]
    head = []
    head = [0, 0, 0]
    head = convert_array2ListNode(head)

    sl = Solution()
    head = sl.deleteDuplicates(head)

    ans = convert_ListNode2array(head)
    print(ans)