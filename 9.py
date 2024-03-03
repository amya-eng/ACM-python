while True:
    try:
        lis = input()
    except:
        exit(0)
    r = 0
    for i in lis:
        i = int(i)
        if i % 2 == 0:
            r += i
    print("%d\n" % r)
