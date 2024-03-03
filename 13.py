# 运行依然错误啊？？
while True:
    try:
        ch, n = input().split()
        n = int(n)
    except:
        exit(0)
    # 先打印第一行
    print((n - 1) * ' ', end="")
    print(ch)
    # 再打印中间的行
    row = 1
    if n - 2 >= 0:
        for i in range(n - 2, 0, -1):
            print(i * ' ', end="")
            print(ch, end="")
            print((2 * (row - 1) + 1) * ' ', end="")
            print(ch)
            row += 1
        # 再打印最后一行
        print(ch * (2 * n - 1))
        print()
