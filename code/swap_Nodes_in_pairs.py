
from typing import List
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if head == None or head.next == None:
            return head
        pre = ListNode('pre')
        res = pre
        pre.next = head
        p = head
        while p != None and p.next != None:
            p1 = p.next
            p2 = p.next.next
            pre.next = p1
            p1.next = p
            p.next = p2
            pre = p
            p = p2
        return res.next


def construct(l):
    head = ListNode('head')
    p = head
    for j in l:
        p.next = ListNode(j)
        p = p.next
    return head.next
def display(node):
    while node:
        print(node.val)
        node = node.next

        
def main():
    l = [1,2,3,4]
    ln = construct(l)
    obj = Solution()
    display(obj.swapPairs(ln))


if __name__ == '__main__':
    main()
