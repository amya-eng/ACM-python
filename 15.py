n = int(input())
while n:
    str1 = input()
    str2 = input()
    n1 = len(str1)//2
    print(str1[:n1] + str2 + str1[n1:])
    n -= 1