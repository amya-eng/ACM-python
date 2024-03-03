class stack():
    def __init__(self):
        self.data = []

    @property
    def l(self):
        return len(self.data)
    def pop(self):
        return None if self.l == 0 else self.data.pop()

    def top(self):
        return None if self.l == 0 else self.data[-1]

    def push(self, value):
        self.data.append(value)


n = int(input())
while n:
    lis = list(map(int, input().split()))
    Stack = stack()
    j = 0
    for i in range(1, n + 1):
        Stack.push(i)
        while Stack.l and Stack.top() == lis[j]:
            Stack.pop()
            j += 1
    if Stack.l == 0:
        print('Yes')
    else:
        print('No')
    n = int(input())