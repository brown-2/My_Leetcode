from typing import List
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
def construct(l: list):
    head = ListNode(l[0])
    p = head
    for i in range(1, len(l)):
        t = ListNode(l[i])
        p.next = t
        p = t
    
    return head

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        p1 = l1
        p2 = l2
        res = ListNode(None)
        pr = res
        while True:
            if p1 == None or p2 == None:
                t = p1 if p1 else p2
                pr.next = t
                break
            if p1.val <= p2.val:
                pr.next = p1
                pr = pr.next
                p1 = p1.next
            else:
                pr.next = p2
                pr = pr.next
                p2 = p2.next
        return res.next


        


def main():
    l1 = [1,2,4]
    l2 = [1,3,4]
    obj = Solution()
    res = obj.mergeTwoLists(construct(l1), construct(l2))
    while res:
        print(res.val)
        res = res.next
    


if __name__ == '__main__':
    main()
