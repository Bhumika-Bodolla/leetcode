class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        m = len(dungeon)
        n = len(dungeon[0])

        dp = [0]*m
        for i in range(m): #creating array
            dp[i] = [0]*n
        
        dp[m-1][n-1] = max(1, 1- dungeon[m-1][n-1]) # 1 case

        for i in range(m-2, -1, -1): #2 case
            dp[i][n-1] = max(1, dp[i+1][n-1] - dungeon[i][n-1])
        for i in range(n-2, -1, -1):    
            dp[m-1][i] = max(1, dp[m-1][i+1] - dungeon[m-1][i])
        
        for i in range(m-2, -1,-1): # 3 case
            for j in range(n-2,-1,-1):
                tmp = min(dp[i+1][j], dp[i][j+1])
                dp[i][j] = max(1, tmp - dungeon[i][j])
                
        return dp[0][0]