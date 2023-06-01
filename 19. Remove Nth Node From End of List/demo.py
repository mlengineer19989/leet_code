# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd_first(self, head: ListNode, n: int) -> ListNode:
        """my first solution

        Args:
            head (ListNode): _description_
            n (int): _description_

        Returns:
            ListNode: _description_
        """
        L = self.ListNode2list(head)
        L.pop(-n)
        return make_ListNode(L)

    def ListNode2list(self, head):
        L = []
        target = head

        while target is not None:
            L.append(target.val)
            target = target.next
        return L

    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        length = self.calc_length(head)

        if length == n:
            return head.next

        ptr = head
        for i in range(1, length - n):
            ptr = ptr.next
        ptr.next = ptr.next.next
        return head

    def calc_length(self, head):
        target = head
        count = 0

        while target:
            target = target.next
            count += 1
        return count

def make_ListNode(head: list):
    if len(head)==0:
        return ListNode("")

    for i, v in enumerate(reversed(head)):
        if i == 0:
            LinearList = ListNode(v)
        else:
            LinearList = ListNode(v, LinearList)
    return LinearList

if __name__ == "__main__":
    # head = [1]
    # n = 1

    head = [1,2,3,4,5]
    n = 2

    ListNode_from_head = make_ListNode(head)
    print(index(ListNode_from_head))

    # sl = Solution()
    # ans = sl.removeNthFromEnd(ListNode_from_head, n)
    # print(ans)