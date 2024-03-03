a, b = input().split(" ")
while True:
    a = int(a)
    b = int(b)
    if a == 0 and b == 0:
        exit(0)
    else:
        print(a + b)
    a, b = input().split(" ")