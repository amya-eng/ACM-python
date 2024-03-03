# 计算二叉树的高度
class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value


class Tree:
    def __init__(self, value):
        self.root = Node(value)


def creat_tree(pre, mid):
    if len(pre) == 0 and len(mid) == 0:
        return None
    tree = Tree(pre[0])
    index = mid.index(pre[0])
    tree.root.left = creat_tree(pre[1:index + 1], mid[: index])
    tree.root.right = creat_tree(pre[index + 1:], mid[index + 1:])
    return tree.root


def get_height(node):
    if node == None:
        return 0
    l = get_height(node.left)
    r = get_height(node.right)
    return l + 1 if l > r else r + 1


while True:
    try:
        n = int(input())
        lis1 = input()
        lis2 = input()
    except:
        exit(0)
    root = creat_tree(lis1, lis2)
    print(get_height(root))