from typing import List
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        rp = head
        for i in range(n):
            rp = rp.next
        if rp == None:
            return head.next
        lp = head
        while True:
            if rp.next == None:
                break
            rp = rp.next
            lp = lp.next
        t = lp.next
        lp.next = lp.next.next
        del t
        return head
        
def main():
    obj = Solution()
    p = ListNode(1)
    head = p
    for i in range(2, 6):
        t = ListNode(i)
        p.next = t
        p = t
    n = 2
    print(obj.removeNthFromEnd(head, 2))



if __name__ == '__main__':
    main()
