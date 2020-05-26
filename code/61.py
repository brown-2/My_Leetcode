from typing import List
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def lenth_of_list(self, head):
        if head == None:
            return 0, None
        t = head
        res = 1
        while t.next != None:
            t = t.next
            res += 1
        return res, t
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if head == None:
            return head
        list_length, tail = self.lenth_of_list(head)
        if k >= list_length:
            k = k % list_length
        if k == 0:
            return head

        index_of_new_tail = list_length - k
        new_tail = head
        for i in range(index_of_new_tail - 1):
            new_tail = new_tail.next
        new_head = new_tail.next
        new_tail.next = None
        tail.next = head
        return new_head


def gene_tree(l):
    head = ListNode(l[0])
    t = head
    for i in l[1:]:
        t.next = ListNode(i)
        t = t.next
    return head
def main():
    l = [1,2,3,4,5]
    k = 2
    head = gene_tree(l)
    obj = Solution()
    new_head = obj.rotateRight(head, k)
    while new_head != None:
        print(new_head.val)
        new_head = new_head.next


if __name__ == '__main__':
    main()
