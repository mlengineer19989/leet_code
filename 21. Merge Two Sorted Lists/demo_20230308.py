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
                v = list1.val
                list1 = list1.next
            else:
                v = list2.val
                list2 = list2.next
            dummyHead.next = ListNode(val=v)
            dummyHead = dummyHead.next

        if list1:
            dummyHead.next = list1
        elif list2:
            dummyHead.next = list2

        return newHead.next


def conv_arr2LN(arr):
    LN = None
    for v in arr[::-1]:
        LN = ListNode(val=v, next=LN)
    return LN

def conv_LN2arr(LN):
    arr = []
    while LN:
        arr.append(LN.val)
        LN = LN.next
    return arr

if __name__ == "__main__":
    list1 = [1,2,4]
    list2 = [1,3,4, 8, 100]

    # list1 = []
    # list2 = []

    # list1 = []
    # list2 = [0]

    list1 = conv_arr2LN(list1)
    list2 = conv_arr2LN(list2)

    sl = Solution()
    ans = sl.mergeTwoLists(list1=list1, list2=list2)
    
    ans = conv_LN2arr(ans)
    print(ans)