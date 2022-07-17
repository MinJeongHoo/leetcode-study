class Solution:
    def climbStairs(self, n: int) -> int:
        arr = [0]*50
        
        arr[1] = 1
        arr[2] = 2
        
        def dp(x):
            if arr[x] != 0:
                return arr[x]
            else:
                arr[x] = dp(x-1) + dp(x-2)
                return arr[x]
        return dp(n)
            
        