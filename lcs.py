def lcs(x,y):
    dp = [[0 for i in range(len(y)+1)] for j in range(len(x)+1)]
    ans = 0
    for i in range(len(x)):
        for j in range(len(y)):
            if x[i]==y[j]:
                dp[i+1][j+1]= (1+dp[i][j])
                ans = max(ans,dp[i+1][j+1])
            else:
                dp[i + 1][j + 1] = 0
    return ans

if __name__ == '__main__':
    x = "OldSite:GeeksforGeeks.org"
    y = "NewSite:GeeksQuiz.com"
    ans = lcs(x,y)
    print ans