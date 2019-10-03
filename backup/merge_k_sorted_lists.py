
from typing import List
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        head = ListNode('head')
        p = head
        while any(lists):
            while None in lists:
                lists.remove(None)
            current = min(lists, key = lambda x: x.val)
            p.next = current
            lists[lists.index(current)] = current.next
            p = p.next
        return head.next
                
        


def construct(l):
    res = []
    for i in l:
        t = ListNode(None)
        p = t
        for j in i:
            p.next = ListNode(j)
            p = p.next
        res.append(t.next)
    return res
def display(node):
    while node:
        print(node.val)
        node = node.next

        
def main():
    l = [[1,4,5], [1,3,4], [2,6]]
    ln = construct(l)
    
    obj = Solution()
    res = obj.mergeKLists(ln)
    display(res)


if __name__ == '__main__':
    main()
