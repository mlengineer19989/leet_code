# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def swapPairs_first(self, head: ListNode) -> ListNode:
        newHead = dummyHead = ListNode()
        oddHead = head.next
        evenHead = head
        cn = 1

        while oddHead and evenHead:
            if cn%2==0:
                dummyHead.next = evenHead
                evenHead = evenHead.next.next if evenHead.next else None
            else:
                dummyHead.next = oddHead
                oddHead = oddHead.next.next if oddHead.next else None

            dummyHead = dummyHead.next
            cn += 1
        
        if oddHead:
            dummyHead.next = oddHead

        if evenHead:
            dummyHead.next =evenHead

        return newHead.next

    def swapPairs_second(self, head: ListNode) -> ListNode:
        newHead = dummyHead = ListNode()
        dummyHead.next = head

        while dummyHead.next and dummyHead.next.next:
            node1 = dummyHead.next
            node2 = dummyHead.next.next
            node3 = dummyHead.next.next.next

            dummyHead.next = node2
            dummyHead.next.next = node1
            dummyHead.next.next.next =node3

            dummyHead = dummyHead.next.next

        return newHead.next

    def swapPairs_recur(self, head: ListNode) -> ListNode:
        newHead = dummyHead = ListNode()
        dummyHead.next = head

        while dummyHead.next and dummyHead.next.next:
            node1 = dummyHead.next
            node2 = dummyHead.next.next
            node3 = dummyHead.next.next.next

            dummyHead.next = node2
            dummyHead.next.next = node1
            dummyHead.next.next.next =node3

            dummyHead = dummyHead.next.next

        return newHead.next

    # def swapPairs(self, head: ListNode) -> ListNode:
    #   if head == None or head.next == None:
    #     return head
    #   new_h = head.next
    #   head.next = self.swapPairs(new_h.next)
    #   new_h.next = head
    #   return new_h

    def swapPairs(self, head: ListNode) -> ListNode:
      new_h = ListNode(None)
      new_h.next = head
      ptr = new_h
      while ptr.next != None and ptr.next.next != None:
        node1, node2, node3 = ptr.next, ptr.next.next, ptr.next.next.next
        ptr.next = node2
        ptr.next.next = node1
        ptr.next.next.next = node3
        ptr = node1
      return new_h.next

def make_ListNode(arr):
    node = None
    for v in arr[::-1]:
        node = ListNode(v, node)
    return node

def print_ListNode2array(node):
    if node:
        arr = []
        while node:
            arr.append(node.val)
            node = node.next
        print(arr)


if __name__ == "__main__":
    head = [1,2,3,4]
    head = make_ListNode(head)

    sl = Solution()
    ans = sl.swapPairs_second(head)

    print_ListNode2array(ans)