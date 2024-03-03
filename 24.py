# 最长公共子序列                         dp表初始化时注意不要用dp = [[0] * (len1 + 1)] * (len2 + 1),这是浅拷贝，数值更新会出问题
while True:
    try:
        lis = list(input().split())
        str1 = list(lis[0])
        str2 = list(lis[1])
    except:
        exit(0)
    len1, len2 = len(str1), len(str2)
    dp = [[0 for i in range(len2 + 1)] for j in range(len1 + 1)]
    for i in range(1, len1 + 1):
        for j in range(1, len2 + 1):
            if str1[i - 1] == str2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = dp[i - 1][j] if dp[i - 1][j] > dp[i][j - 1] else dp[i][j - 1]
    print(dp[len1][len2])