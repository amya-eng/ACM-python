dic = {'A': 4, 'B':3, 'C':2, 'D':1, 'F':0}
while True:
    try:
        lis = map(str, input().split())
    except:
        exit(0)
    n, r = 0, 0
    flg = 0
    for i in lis:
        if i in dic.keys():
            r += dic[i]
            n += 1
        else:
            flg = 1
            break
    if(flg):
        print('Unknown')
    else:
        print("%.2f" % (r / n))