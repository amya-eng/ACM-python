n = int(input())
while n:
    lis = input().split()
    r_lis = ""
    for i in lis:
        r_lis += i[0].upper()
    print(r_lis)
    n -= 1