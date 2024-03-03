class node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Link:
    def __init__(self, head):
        self.head = head
        self.length = 0
        self.r = self.head

    def insert(self, lis):
        for i in lis:
            node1 = node(i)
            node1.next = self.r.next
            self.r.next = node1
            self.r = node1

    def show(self):
        cur = self.head.next
        while cur:
            print("%d" % cur.value, end=" ")
            cur = cur.next
        print()

    def delete_repeat(self):
        p = self.head.next
        if p:
            q = p.next
            while q:
                if p.value == q.value:
                    p.next = q.next
                    q = p.next
                else:
                    p = q
                    q = q.next


while True:
    try:
        lis = list(map(int, input().split()))
    except:
        exit(0)
    if lis[0]:
        head = node(-1)
        link = Link(head)
        link.insert(lis[1:])
        link.show()
        link.delete_repeat()
        link.show()
    else:
        print("list is empty")