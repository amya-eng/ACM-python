# A + B 问题
a, b = input().split()
while True:
    a = int(a)
    b = int(b)
    print(a+b)
    try:
        a, b = input().split()
    except:
        exit(0)