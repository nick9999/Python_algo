class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def morris_inorder(root):
    curr = root
    while curr:
        if curr.left is None:
            print curr.val
            print ' '
            curr = curr.right

        else:
            prev = curr.left
            while prev.right is not None and prev.right !=curr:
                prev = prev.right

            # Threading is already there
            if prev.right is not None:
                prev.right = None
                print curr.val
                print ' '
                curr = curr.right

            else:
                prev.right = curr
                curr = curr.left

def recover_bst(root):
    pre = None
    first = None
    second = None

    curr = root
    while curr:
        if curr.left is None:
            if pre is not None and pre.val > curr.val:
                if first is None:
                    first = pre
                    second = curr
                else:
                    second = curr
            pre = curr
            curr = curr.left

        else:
            tmp = curr.left
            while tmp.right is not None and tmp.right != curr:
                tmp = tmp.right

            if tmp.right is not None:
                tmp.right = None
                if pre is not None and pre.val > curr.val:
                    if first is None:
                        first = pre
                        second = curr
                    else:
                        second = curr
                pre = curr
                curr = curr.right

            else:
                tmp.right = curr
                curr = curr.left
    if first is not None and second is not None:
        t = first.val
        first.val = second.val
        second.val = t



if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)

    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)

    root.right.left = TreeNode(6)
    root.right.right = TreeNode(7)

    root.left.left.left = TreeNode(8)
    root.left.left.right = TreeNode(9)

    root.left.right.left = TreeNode(10)
    root.left.right.right = TreeNode(11)

    morris_inorder(root)