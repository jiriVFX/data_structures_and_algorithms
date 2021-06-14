# https://leetcode.com/problems/min-cost-climbing-stairs/
# You are given an integer array cost where cost[i] is the cost of ith step on a staircase.
# Once you pay the cost, you can either climb one or two steps.
# You can either start from the step with index 0, or the step with index 1.
# Return the minimum cost to reach the top of the floor.

def minCostClimbingStairs(cost):
    """
    :type cost: List[int]
    :rtype: int
    """
    accumulated_costs = []

    for i in range(len(cost)):
        if i > 1:
            current_cost = cost[i] + min(accumulated_costs[i - 1], accumulated_costs[i - 2])
        else:
            # no previous costs
            current_cost = cost[i]
        # add minimum cost at the current step to accumulated_costs
        accumulated_costs.append(current_cost)
    # return minimum of the last two steps (we can choose to start from 0 or 1 - first or second step)
    return min(accumulated_costs[-1], accumulated_costs[-2])


print(minCostClimbingStairs([10, 15, 20]))
print(minCostClimbingStairs([1, 100, 1, 1, 1, 100, 1, 1, 100, 1]))
