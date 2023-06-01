#Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def making_ListNode(L):
    head = None
    for v in L:
        head = ListNode(val=v, next=head)

    return head

class Solution:
    """my first solution
    """
    def middleNode(self, head):

        L = []
        current_node = head
        while True:
            L.append(current_node.val)

            if current_node.next is None:
                break

            current_node = current_node.next

        L.reverse()

        n = len(L)
        if n%2==1:
            new_L = L[n//2:]
        else:
            new_L = L[n//2:]


        print(L, new_L)
        new_head = making_ListNode(new_L)


        return new_head

    

class Solution_approach1:
    def middleNode(self, head: ListNode) -> ListNode:
        arr = [head]
        while arr[-1].next:
            arr.append(arr[-1].next)
        return arr[len(arr) // 2]

class Solution_approach2:
    def middleNode(self, head):
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow



if __name__=="__main__":
    head = making_ListNode([1,2,3,4,5])
    test = Solution_approach1()
    ans = test.middleNode(head)
    print(ans)