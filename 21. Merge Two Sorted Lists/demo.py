# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists_first(self, list1: ListNode, list2: ListNode) -> ListNode:
        mergedList = list1
        CN1 = mergedList
        CN2 = list2

        while CN2:
            print(CN1.val, CN2.val)
            if CN1.val > CN2.val:
                CN1.next = CN1
                CN1.val = CN2.val
                CN2 = CN2.next
            else:
                CN1 = CN1.next

        return mergedList

    def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:
        newHead = dummyHead = ListNode()
        while list1 and list2:
            if list1.val < list2.val:
                dummyHead.next = list1
                list1 = list1.next
            else:
                dummyHead.next = list2
                list2 = list2.next
            dummyHead = dummyHead.next
            print_result(newHead.next)
        
        if list1:
            dummyHead.next = list1
        if list2:
            dummyHead.next = list2
        return newHead.next


    def mergeTwoLists_second(self, list1: ListNode, list2: ListNode) -> ListNode:
        #mergedList = list1
        newHead = CN1 = list1
        CN2 = list2

        while CN1 and CN2:
            if CN1.val > CN2.val:
                CN1 = CN2
                #この書き方だと、newHeadのまで変更されない。

                CN2 = CN2.next
            
            CN1 = CN1.next
            print_result(CN1)

        return newHead

    def mergeTwoLists_third(self, list1: ListNode, list2: ListNode) -> ListNode:
        newHead = dummy = ListNode()

        while list1 and list2:
            if list1.val <= list2.val:
                dummy.next = list1
                list1 = list1.next
            else:
                dummy.next = list2
                list2 = list2.next
            dummy = dummy.next
            
        if list1:
            dummy.next = list1

        
        if list2:
            dummy.next = list2


        return newHead.next

    

                

def make_ListNode(L:list):
    listnode = None
    for v in L[::-1]:
        listnode = ListNode(val=v, next=listnode)
    return listnode

def print_result(L):
    if L:
        ans = []
        while L:
            ans.append(L.val)
            L = L.next
        print(ans)

if __name__ == "__main__":
    list1 = [1,2,4]
    list2 = [1,3,4]

    list1 = make_ListNode(list1)
    list2 = make_ListNode(list2)
    

    sl = Solution()
    #ans = sl.mergeTwoLists(list1, list2)
    ans = sl.mergeTwoLists_third(list1, list2)
    print_result(ans)