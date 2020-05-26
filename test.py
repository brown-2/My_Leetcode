from typing import List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if not preorder:
            return None
        root = TreeNode(preorder[0])
        index = inorder.index(root.val)
        l_inorder = inorder[:index]
        r_inorder = inorder[index + 1:]

        l_preorder = preorder[1:1 + len(l_inorder)]
        r_preorder = preorder[index + 1:index + 1 + len(r_inorder)]

        root.left = self.buildTree(l_preorder, l_inorder)
        root.right = self.buildTree(r_preorder, r_inorder)
        return root
            
def print_tree(root):
    if root == None:
        print('null', end = ' ')
    else:
        print(root.val, end = ' ')
        print_tree(root.left)
        print_tree(root.right)

def main():
    obj = Solution()
    preorder = [3,9,20,15,7]
    inorder = [9,3,15,20,7]
    preorder = [1,2,3]
    inorder = [3,2,1]
    tree = obj.buildTree(preorder, inorder)
    print_tree(tree)



if __name__ == '__main__':
    main()
