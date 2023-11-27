class Solution:
    def findLength(self, A, B):
        
        if not A or not B:
            return 0
        
        print(self.lcs(A,B))

        return self.lcs(A,B)
        
    def lcs(self,a,b):
        n = len(a)
        m = len(b)
        
        dp = [[0]*(n+1) for i in range(m+1)]
        res = 0
        
        for i in range(1,n+1):
            for j in range(1,m+1):
                
                if a[i-1] == b[j-1]:
                    dp[i][j] = 1 + dp[i-1][j-1]
                    res = max(res,dp[i][j])
                    
                else:
                    dp[i][j] = 0
                    
        return res


obj = Solution()

obj.findLength("abcde", "ace")
