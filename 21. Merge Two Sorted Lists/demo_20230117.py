# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:
        newHead = dummyHead = ListNode()
        
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

        if list2:
            dummyHead.next = list2

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
    # list1 = [1,2,4]
    # list2 = [1,3,4]

    list1 = []
    list2 = [0]

    list1 = convert_array2ListNode(list1)
    list2 = convert_array2ListNode(list2)

    sl = Solution()
    ans = sl.mergeTwoLists(list1, list2)

    ans = convert_ListNode2array(ans)
    print(ans)