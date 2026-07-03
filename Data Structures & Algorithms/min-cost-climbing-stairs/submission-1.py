class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        current_cost = 0
        prev2_cost = cost[0]
        prev1_cost = cost[1]

        for i in range(2,len(cost)):
            current_cost = min(prev1_cost, prev2_cost) + cost[i]
            prev2_cost = prev1_cost
            prev1_cost = current_cost

        current_cost = min(prev1_cost, prev2_cost)
        
        if len(cost) <= 1:
            return 0
        else:
            return current_cost

            