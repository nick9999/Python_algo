def max_profit(price,k):
    """
    This is O(Kn^2) solution
    """
    n = len(price)
    dp = [[0 for i in range(k+1)] for j in range(n)]
    print dp
    for i in range(1,n):
        for j in range(1,k+1):
            tmp = 0
            for l in range(i):
                tmp = max(tmp,price[i]-price[l]+dp[l][j-1])
            dp[i][j] = max(dp[i-1][j],tmp)
    return dp[n-1][k]

def max_profit_2(price,k):
    """
        This is O(KN) solution
    """
    n = len(price)
    dp = [[0 for i in range(k+1)] for j in range(n)]
    for i in range(1,k+1):
        tmp = -float("inf")
        for j in range(1,n):
            tmp = max(tmp,dp[j-1][i-1]-price[j-1])
            dp[j][i] = max(dp[j-1][i],tmp+price[j])
    return dp[n-1][k]

if __name__ == '__main__':
    price = [12, 14, 17, 10, 14, 13, 12, 15]
    ans = max_profit_2(price,3)
    print ans