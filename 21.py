class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value


class Tree:
    def __init__(self, value):
        self.root = Node(value)


def print_by_back(root):
    if root == None:
        return
    print_by_back(root.left)
    print_by_back(root.right)
    print(root.value, end="")


def creat_tree(pre, mid):
    if len(pre) == 0 and len(mid) == 0:
        return None
    tree = Tree(pre[0])
    index = mid.index(pre[0])
    tree.root.left = creat_tree(pre[1:index + 1], mid[: index])
    tree.root.right = creat_tree(pre[index + 1:], mid[index + 1:])
    return tree.root


while True:
    try:
        lis = input().split()
    except:
        exit(0)
    root = creat_tree(lis[0], lis[1])
    print_by_back(root)
    print()