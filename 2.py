sum = int(input())
while sum:
    while sum:
        a, b = input().split()
        a  = int(a)
        b = int(b)
        print(a + b)
        sum -= 1
    try:
        sum = int(input())
    except:
        exit(0)