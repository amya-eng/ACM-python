lis = list(map(int, input().split(" ")))
while lis[0]:
    sum = 0
    for i in lis[1:]:
        sum += int(i)
    print(sum)
    try:
        lis = list(map(int, input().split(" ")))
    except:
        exit(0)