# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, list1: ListNode, list2: ListNode) -> ListNode:
        newHead = dummyHead = ListNode()
        carry = 0

        while list1 or list2 or carry>0:
            dummyHead.next = ListNode()
            dummyHead = dummyHead.next

            v1 = list1.val if list1 else 0
            v2 = list2.val if list2 else 0

            num = v1 + v2 + carry
            dummyHead.val = num%10
            carry = num//10
            
            list1 = list1.next if list1 else list1
            list2 = list2.next if list2 else list2

        return newHead.next


def convert_array2ListNode(arr: list):
    ln = None
    for v in arr[::-1]:
        ln = ListNode(val=v, next=ln)

    return ln

def convert_ListNode2array(head: ListNode):
    arr = []
    while head:
        arr.append(head.val)
        head = head.next
    return arr

if __name__ == "__main__":
    l1 = [2,4,3]
    l2 = [5,6,4]

    # l1 = [0]
    # l2 = [0]

    # l1 = [9,9,9,9,9,9,9]
    # l2 = [9,9,9,9]

    l1 = convert_array2ListNode(l1)
    l2 = convert_array2ListNode(l2)


    sl = Solution()
    ans = sl.addTwoNumbers(l1, l2)
    ans = convert_ListNode2array(ans)
    print(ans)