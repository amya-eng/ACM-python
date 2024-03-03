row = int(input())
while row:
    while row:
        lis = list(map(int, input().split()))
        if lis[0]:
            ans = 0
            for i in lis[1:]:
                ans += i
            if row != 1:
                print(ans, end="\n\n")
            else:
                print(ans, end="\n")

        row -= 1
    try:
        row = int(input())
    except:
        exit(0)
