class node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Link:
    def __init__(self, head):
        self.head = head
        self.length = 0
        self.r = head

    def insert(self, lis):
        for i in lis:
            node1 = node(i)
            node1.next = self.r.next
            self.r.next = node1
            self.r = node1

    def reverse(self):
        p = self.head.next
        if p is None:
            return None
        q = p.next
        p.next = None
        while q:
            r = q.next
            q.next = p
            p = q
            q = r
            if r:
                r = r.next
        head.next = p

    def show(self):
        cur = self.head.next
        if cur == None:
            print("list is empty")
            return
        while cur:
            print("%d" % cur.value, end=" ")
            cur = cur.next
        print()



while True:
    try:
        lis = list(map(int, input().split()))
    except:
        exit(0)
    if lis[1:]==[]:
        print('list is empty')
        continue
    head = node(None)
    link = Link(head)
    link.insert(lis[1:])
    link.show()
    link.reverse()
    link.show()