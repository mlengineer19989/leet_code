# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        ln = rn = head
        for i in range(right):
            rn = rn.next

        if left > 2:
            for i in range(left-2):
                ln = ln.next

        

        c1 = ln.next
        c2 = ln.next.next
        c3 = ln.next.next.next
        c1.next = rn

        while c2!=rn:
            c2.next = c1
            c1 = c2
            c2 =c3
            c3 = c3.next if c3 else c3

        
        ln.next = c1

        return head


def convert_array2ListNode(arr):
    head = None
    for v in arr[::-1]:
        head = ListNode(val=v, next=head)
    return head

def convert_ListNode2array(head):
    arr = []
    cnt = 0
    while head or cnt<10:
        arr.append(head.val)
        head = head.next
        cnt += 1
    return arr

if __name__ == "__main__":
    head = [1,2,3,4,5]
    left = 2
    right = 4

    ans = convert_array2ListNode(head)

    sl = Solution()
    ans = sl.reverseBetween(ans, left, right)

    ans = convert_ListNode2array(ans)
    print(ans)