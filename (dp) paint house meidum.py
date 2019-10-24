class Solution:
    """
    @param costs: n x 3 cost matrix
    @return: An integer, the minimum cost to paint all houses
    """
    def minCost(self, costs):
        # write your code here
        # total cost include this and options
        if not costs:
            return 0 
            
        dp = [[sys.maxsize] * 3 for _ in costs]
        
        for i, cost in enumerate(costs):
            if i ==0:
                dp[i] = cost 
            
            else:
                dp[i][0] = min(dp[i-1][1], dp[i-1][2]) + cost[0]
                dp[i][1] = min(dp[i-1][0], dp[i-1][2]) + cost[1]
                dp[i][2] = min(dp[i-1][0], dp[i-1][1]) + cost[2]
                
        
        return min(dp[-1])





# method 2 less space

class Solution:
    """
    @param costs: n x 3 cost matrix
    @return: An integer, the minimum cost to paint all houses
    """
    def minCost(self, costs):
        # write your code here
        # total cost include this and options
        if not costs:
            return 0 
            
        dp = [sys.maxsize] * 3
        
        for i, cost in enumerate(costs):
            if i ==0:
                dp = cost 
            
            else:
                copy = dp[:]
                dp[0] = min(copy[1], copy[2]) + cost[0]
                dp[1] = min(copy[0], copy[2]) + cost[1]
                dp[2] = min(copy[0], copy[1]) + cost[2]
                
        
        return min(dp)