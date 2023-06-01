# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if head is None or head.next is None:
            return head

        n1 = head
        n2 = n1.next
        n3 = n1.next.next
        n1.next = None

        while n2:
            n2.next = n1

            n1 = n2
            n2 = n3
            if n3:
                n3 = n3.next
        return n1

def convert_array2ListNode(arr):
    head = None
    for v in arr[::-1]:
        head = ListNode(val=v ,next=head)
    return head

def convert_ListNode2array(head):
    arr = []
    while head:
        arr.append(head.val)
        head = head.next
    return arr

if __name__ == "__main__":
    head = [1,2,3,4,5]
    head = [1,2]
    head = [0, 1]

    ans = convert_array2ListNode(head)

    sl = Solution()
    ans = sl.reverseList(ans)

    ans = convert_ListNode2array(ans)
    print(ans)