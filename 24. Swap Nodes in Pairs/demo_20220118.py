# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        newHead = dummyHead = ListNode()
        dummyHead.next = head

        while dummyHead.next and dummyHead.next.next:
            node1 = dummyHead.next
            node2 = dummyHead.next.next
            node3 = dummyHead.next.next.next

            dummyHead.next = node2
            dummyHead.next.next = node1
            dummyHead.next.next.next = node3

            dummyHead = dummyHead.next.next

        return newHead.next

def convert_array2ListNode(arr):
    LN = None
    for v in arr[::-1]:
        LN = ListNode(val=v, next=LN)

    return LN

def convert_ListNode2array(head):
    arr = []
    while head:
        arr.append(head.val)
        head = head.next
    return arr

if __name__ == "__main__":
    #head = [1,2,3,4]
    head = [1]
    head = convert_array2ListNode(head)

    sl = Solution()
    ans = sl.swapPairs(head)

    ans = convert_ListNode2array(ans)
    print(ans)