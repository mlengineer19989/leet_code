# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        length = 1
        dummyHead = head
        while dummyHead:
            dummyHead = dummyHead.next
            length += 1

        newHead = dummyHead = ListNode()
        dummyHead.next = head
        for i in range(length-n-1):
            #dummyノードを次のノードに移動させる
            dummyHead = dummyHead.next
        #dummyノードの次のノードを変更する。この変更は、newHeadにも反映される。
        dummyHead.next = dummyHead.next.next
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
    # head = [1,2,3,4,5]
    # n = 2

    # head = [1]
    # n = 1

    head = [1,2]
    n = 1

    head = convert_array2ListNode(head)

    sl = Solution()
    ans = sl.removeNthFromEnd(head, n)

    ans = convert_ListNode2array(ans)
    print(ans)