while True:
    try:
        n = int(input())
    except:
        exit(0)
    dic = dict()
    while n:
        k, v = input().split()
        dic[k] = v
        n -= 1
    ming_lis = []
    key_item = '1'
    while key_item in dic.keys():
        ming_lis.append(dic[key_item])
        key_item = dic[key_item]
    yu_lis = []
    key_item = '2'
    yu_anc = -1
    while key_item in dic.keys():
        yu_anc += 1
        anc = dic[key_item]
        if anc in ming_lis:
            ming_anc = ming_lis.index(anc)
            break
        key_item = dic[key_item]
    if yu_anc < ming_anc:
        print('You are my elder')
    elif yu_anc > ming_anc:
        print('You are my younger')
    else:
        print('You are my brother')