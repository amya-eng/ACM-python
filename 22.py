class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value


class Tree:
    def __init__(self):
        self.root = None

    def add_node(self, father, pos, value):          # 值为father的pos儿子（0左1右）值为value
        node = Node(value)
        queue = [self.root]
        while queue:
            cur = queue[0]
            del queue[0]  # 队列的实现：删除第一个元素 del q[0]
            if cur.value == father and pos == 0:
                cur.left = node
                break
            elif cur.value == father and pos == 1:
                cur.right = node
                break
            else:
                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)



def print_by_mid(root):
    if root == None:
        return
    print_by_mid(root.left)
    print(root.value, end="")
    print_by_mid(root.right)


def print_by_forward(root):
    if root == None:
        return
    print(root.value, end="")
    print_by_forward(root.left)
    print_by_forward(root.right)


def print_by_back(root):
    if root == None:
        return
    print_by_back(root.left)
    print_by_back(root.right)
    print(root.value, end="")


n = int(input())
lis = []
while n:
    lis1 = input().split()
    lis1[1] = int(lis1[1]) - 1
    lis1[2] = int(lis1[2]) - 1            # 全部转化为数组下标序列
    lis.append(lis1)
    n -= 1
tree = Tree()
tree.root = Node(lis[0][0])
queue = [0]                   # 存放父亲元素的下标
while queue:
    cur = queue[0]
    del queue[0]
    l = lis[cur][1]
    r = lis[cur][2]
    if l != -1:
        queue.append(l)
        tree.add_node(lis[cur][0], 0, lis[l][0])
    if r != -1:
        queue.append(r)
        tree.add_node(lis[cur][0], 1, lis[r][0])
print_by_forward(tree.root)
print()
print_by_mid(tree.root)
print()
print_by_back(tree.root)
print()