str1 = "abcdefg"
str2 = "ace"
len1, len2 = len(str1), len(str2)
print(len1, len2)
dp = [[0] * len1] * len2

dp[1][1] = 3
print(dp)
