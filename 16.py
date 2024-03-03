n = int(input())
while n:
    str1 = list(input().split())
    index = 0
    for i in str1:
        if index % 2 == 0:
            str1[index] = str1[index + 1]
            str1[index + 1] = i
        else:
            pass
        index += 1
    print("".join(str1))
    n -= 1