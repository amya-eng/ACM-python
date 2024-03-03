n = int(input())
while n:
    lis = list(map(int, input().split()))
    ave = sum(lis) / len(lis)
    r = 0
    for i in lis:
        if i < ave:
            r += ave - i
    print("%d\n" % r)
    n = int(input())