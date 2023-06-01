#Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def making_test_case(L):
    head = None
    for v in L:
        head = ListNode(val=v, next=head)

    return head



def isPalindrome_my_anser(head) -> bool:
    """This method is my first answer.

    Args:
        head (Optional[ListNode]): _description_

    Returns:
        bool: _description_
    """
    L = []
    current_node = head
    while True:
        L.append(current_node.val)

        if current_node.next is None:
            break

        current_node = current_node.next

    R = L.copy()

    R.reverse()


    return L==R




if __name__=="__main__":
    head = making_test_case([1, 2, 2, 1])
    print(isPalindrome_my_anser(head=head))