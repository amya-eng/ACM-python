while True:
    m, k = input().split()
    m = int(m)
    k = int(k)
    m_copy = m
    if m == 0 and k == 0:
        exit(0)
    r = m // k
    m = m % k
    cur = r
    while m + cur >= k:
        m1 = m
        m = (m + cur) // k
        cur = (m1 + cur) % k
        r += m
    print("%d" % (r + m_copy))