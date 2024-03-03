class node:

    def __init__(self, value):
        self.value = value
        self.next = None


class Link:

    def __init__(self, head: node):
        self.head = head
        self.length = 0

    def insert(self, node):
        node.next = self.head.next
        self.head.next = node
        self.length += 1

    def insert_i(self, value, index):
        if index < 0 or index > self.length + 1:
            return None
        else:
            cur = self.head
            for i in range(index - 1):
                cur = cur.next
            node1 = node(value)
            node1.next = cur.next
            cur.next = node1
            self.length += 1
            return 1

    def delete(self, index):
        if index < 0 or index > self.length:
            return None
        else:
            cur = self.head
            for i in range(index - 1):
                cur = cur.next
            cur.next = cur.next.next
            self.length -= 1
            return 1                              # 没有返回值则默认返回None诶

    def get_a(self, index):
        if index < 0 or index > self.length:
            return None
        else:
            cur = self.head
            for i in range(index):
                cur = cur.next
            return cur.value

    def show(self):
        cur = self.head.next
        while cur:
            print(cur.value, end=" ")
            cur = cur.next
        print()


head = node(0)
link = Link(head)
lis = list(map(int, input().split()))
for i in lis[1:]:
    node1 = node(i)
    link.insert(node1)
# 输入链表完毕

n = int(input())
while (n):
    s = input().split()
    if s[0] == 'show':
        if link.length == 0:
            print("Link list is empty")
        else:
            link.show()
    elif s[0] == 'delete':
        if link.delete(int(s[1])) == None:
            print("delete fail")
        else:
            print("delete OK")
    elif s[0] == 'insert':
        if link.insert_i(int(s[2]), int(s[1])) == None:
            print("insert fail")
        else:
            print("insert OK")
    elif s[0] == 'get':
        r = link.get_a(int(s[1]))
        if r == None:
            print("get fail")
        else:
            print("%d" % r)
    n -= 1