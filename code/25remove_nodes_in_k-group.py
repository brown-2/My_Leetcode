
from typing import List
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def f(self, pre, head, k):
        new_head = head
        for i in range(k - 1):
            try:
                new_head = new_head.next
            except AttributeError:
                return None
        if new_head == None:
            return None
        new_pre = head
        curr_head = head
        for i in range(k - 1):
            t = curr_head
            curr_head = curr_head.next
            t.next = new_head.next
            new_head.next = t
        pre.next = new_head
        return new_pre

        
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        res = ListNode('head')
        res.next = head
        new_pre = res
        while new_pre != None:
            new_pre = self.f(new_pre, new_pre.next, k)
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
    l = [1, 2, 3, 4, 5]
    k = 3
    ln = construct(l)
    obj = Solution()
    display(obj.reverseKGroup(ln, k))


if __name__ == '__main__':
    main()
