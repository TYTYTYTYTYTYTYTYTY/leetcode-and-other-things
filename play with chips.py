class Solution:
    def minCostToMoveChips(self, chips: List[int]) -> int:
        if not chips:
            return 0 
        
        mini_cost = sys.maxsize 
        
        for i, pos1 in enumerate(chips):
            temp_cost =0 
            for pos2 in chips[:i] + chips[i+1:]:
                temp_cost += abs(pos2-pos1)%2 
                
            mini_cost  = min(mini_cost, temp_cost)
            
            
            
        return mini_cost