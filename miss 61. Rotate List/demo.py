# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def rotateRight_first(self, head: ListNode, k: int) -> ListNode:
        if head is None or k ==0:
            return head

        dummyHead1 = ListNode()
        dummyHead1.next = head
        length = 0
        while dummyHead1.next:
            dummyHead1 = dummyHead1.next
            length += 1

        k = k%length

        dummyHead1 = ListNode()
        dummyHead1.next = head

        for i in range(length -k +1):
            dummyHead1 = dummyHead1.next
        
        newHead = dummyHead2 = ListNode(val=dummyHead1.val, next=head)

        for i in range(length):
            dummyHead2 = dummyHead2.next
        dummyHead2.next = None


        return newHead

    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        
        if not head:
            return None
        
        lastElement = head
        length = 1
        # get the length of the list and the last node in the list
        while ( lastElement.next ):
            lastElement = lastElement.next
            length += 1

        # If k is equal to the length of the list then k == 0
        # ElIf k is greater than the length of the list then k = k % length
        k = k % length
            
        # Set the last node to point to head node
        # The list is now a circular linked list with last node pointing to first node
        lastElement.next = head
        
        # Traverse the list to get to the node just before the ( length - k )th node.
        # Example: In 1->2->3->4->5, and k = 2
        #          we need to get to the Node(3)
        tempNode = head
        for _ in range( length - k - 1 ):
            tempNode = tempNode.next
        
        # Get the next node from the tempNode and then set the tempNode.next as None
        # Example: In 1->2->3->4->5, and k = 2
        #          tempNode = Node(3)
        #          answer = Node(3).next => Node(4)
        #          Node(3).next = None ( cut the linked list from here )
        answer = tempNode.next
        tempNode.next = None
        
        return answer


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
    head = [1]
    k = 1

    head = convert_array2ListNode(head)

    sl = Solution()
    ans = sl.rotateRight_first(head, k)

    ans = convert_ListNode2array(ans)
    print(ans)