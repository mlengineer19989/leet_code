from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def make_ListNode(l):
    ans = None
    for v in reversed(l):
        ans = ListNode(v, ans)

    return ans

        
class Solution:
    "my first solution"
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        list_class1 = l1
        list_class2 = l2
        next_add_val = 0
        ans_list = []

        while True:
            
            if list_class1 is None:
                val = list_class2.val + next_add_val
                list_class2 = list_class2.next
            elif list_class2 is None:
                val = list_class1.val + next_add_val
                list_class1 = list_class1.next
            else:
                val = list_class1.val + list_class2.val + next_add_val
                list_class1 = list_class1.next
                list_class2 = list_class2.next

            s = str(val)
            if len(s)>1:
                ans_list.append(int(s[1]))
                next_add_val = int(s[0])
            else:
                ans_list.append(val)
                next_add_val = 0

            if (list_class1 is None) and (list_class2 is None):
                if next_add_val>0:
                    ans_list.append(next_add_val)
                break


        ans_list.reverse()
        ans = None
        for v in ans_list:
            ans = ListNode(v, ans)


        return ans


if __name__ == "__main__":
    l1 = make_ListNode([9,9,9,9,9,9,9])
    l2 = make_ListNode([9,9,9,9])

    sl = Solution()
    ans = sl.addTwoNumbers(l1, l2)