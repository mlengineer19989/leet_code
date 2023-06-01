# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if head is None:
            return head

        dummyHead = ListNode(val=None)
        newHead = currentHead =ListNode()
        dummyHead.next = head

        while dummyHead.next.next:
            l = dummyHead.val
            m = dummyHead.next.val
            r = dummyHead.next.next.val

            if l != m and m!=r:
                currentHead.next = ListNode(val=m)
                currentHead = currentHead.next
            
            dummyHead = dummyHead.next

        if dummyHead.next:
            l = dummyHead.val
            m = dummyHead.next.val

            if l != m:
                currentHead.next = ListNode(val=m)

        return newHead.next

def convert_array2ListNode(arr):
    LN = None
    for v in arr[::-1]:
        LN = ListNode(val=v, next=LN)
    return LN

def convert_ListNode2array(LN: ListNode):
    arr = []
    while LN:
        arr.append(LN.val)
        LN = LN.next
    return arr

if __name__ == "__main__":
    head = [1,2,3,3,4,4,5]
    head = [1,1,1,2,3]
    head = []

    ans = convert_array2ListNode(head)

    sl = Solution()
    ans = sl.deleteDuplicates(ans)

    ans = convert_ListNode2array(ans)
    print(ans)