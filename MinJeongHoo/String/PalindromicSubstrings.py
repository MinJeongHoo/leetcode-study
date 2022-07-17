class Solution:
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        res = 0
        dp = [[0]*(n) for i in range(n)]
        for i in range(n-1, -1, -1):
            for j in range(i, n):
                if s[i]==s[j] and (j-i<2 or dp[i+1][j-1]):
                    dp[i][j] = 1
                else:
                    dp[i][j] = 0

                if dp[i][j]:
                    res+=1
        return res 
        