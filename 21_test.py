class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value

class Tree:
    def __init__(self):
        self.root = None

    def add_node(self, lis):
        for value in lis:
            node = Node(value)
            if self.root == None:
                self.root = node
                continue
            queue = [self.root]
            while queue:
                cur = queue[0]
                del queue[0]                        # 队列的实现：删除第一个元素 del q[0]
                if cur.left == None:
                    cur.left = node
                    break
                elif cur.right == None:
                    cur.right = node
                    break
                else:
                    queue.append(cur.left)
                    queue.append(cur.right)

def print_by_mid(root):
    if root == None:
        return
    print_by_mid(root.left)
    print(root.value, end=" ")
    print_by_mid(root.right)

def print_by_forward(root):
    if root == None:
        return
    print(root.value, end=" ")
    print_by_forward(root.left)
    print_by_forward(root.right)


def print_by_back(root):
    if root == None:
        return
    print_by_back(root.left)
    print_by_back(root.right)
    print(root.value, end=" ")

lis = list(map(int, input().split()))
tree = Tree()
tree.add_node(lis)
print('mid:')
print_by_mid(tree.root)
print()
print('forward:')
print_by_forward(tree.root)
print()
print('back:')
print_by_back(tree.root)
print()




