from typing import List
class Node:
    def __init__(self, value, next_node = None):
        self.value = value
        self.next_node = next_node
def generate_tree(l:List[int]):
    head = Node(l[0])
    current_Node = head
    for i in l[1:]:
        current_Node.next_node = Node(i)
        current_Node = current_Node.next_node
    return head
def print_tree(head):
    current_node = head
    while current_node != None:
        print(current_node.value)
        current_node = current_node.next_node
def sort2tree(head1, head2):
    if head2.value < head1.value:
        tem = head2
        head2 = head1
        head1 = tem
    current2 = head2
    smaller = head1
    bigger = head1.next_node
    while current2 != None and bigger != None:
        while bigger.value < current2.value:
            if bigger.next_node == None:
                bigger.next_node = current2
                break
            else:
                smaller = bigger
                bigger = bigger.next_node
        tem = current2
        current2 = current2.next_node
        tem.next_node = bigger
        smaller.next_node = tem
        smaller = tem
    return head1




if __name__ == '__main__':
    l1 = [1, 3, 5, 7, 8, 9]
    l2 = [2, 4, 6, 7]
    tree1 = generate_tree(l1)
    tree2 = generate_tree(l2)
    head = sort2tree(tree1, tree2)
    print_tree(head)
    
