while True:
    try:
        n = int(input())
    except:
        exit(0)
    i = 1
    for i in range(1, 2 * n):
        space = n - i if i < n else i % n
        print(space * ' ', end="")
        for j in range(n - space):
            print(j + 1, end="")
        for j in range(n - space - 1, 0, -1):
            print(j, end="")
        print()