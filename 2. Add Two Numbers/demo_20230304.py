# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, list1: ListNode, list2: ListNode) -> ListNode:
        carry = 0
        newHead = dummyHead = ListNode()

        while list1 or list2:
            v1 = list1.val if list1 else 0
            v2 = list2.val if list2 else 0

            sum = v1 + v2 +carry
            carry = sum // 10
            v = sum - carry * 10

            dummyHead.next = ListNode(val=v)
            dummyHead = dummyHead.next

            list1 = list1.next if list1 else list1
            list2 = list2.next if list2 else list2

        if carry > 0:
            dummyHead.next = ListNode(val=carry)

        return newHead.next


    
def conv_list2LN(arr : list[int]):
    LN = None
    for v in arr[::-1]:
        LN = ListNode(val=v, next=LN)
    return LN

def conv_LN2list(LN : ListNode):
    arr = []
    while LN:
        arr.append(LN.val)
        LN = LN.next
    return arr
    
if __name__ == "__main__":
    l1 = [2,4,3]
    l2 = [5,6,4]

    # l1 = [0]
    # l2 = [0]

    # l1 = [9,9,9,9,9,9,9]
    # l2 = [9,9,9,9]

    LN1 = conv_list2LN(l1)
    LN2 = conv_list2LN(l2)

    sl = Solution()
    ans = sl.addTwoNumbers(list1=LN1, list2=LN2)

    ans = conv_LN2list(ans)
    print(ans)