class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :param cost:List[int]
        :return:int
        """
        cost_0, cost_1 = cost[0], cost[1]
        for s in cost[2:]:
            current_cost = min(cost_0,cost_1) + s
            cost_0,cost_1 = cost_1,current_cost
        return min(cost_0,cost_1)
