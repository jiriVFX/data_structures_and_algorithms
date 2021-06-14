# https://leetcode.com/problems/min-cost-climbing-stairs/
# You are given an integer array cost where cost[i] is the cost of ith step on a staircase.
# Once you pay the cost, you can either climb one or two steps.
# You can either start from the step with index 0, or the step with index 1.
# Return the minimum cost to reach the top of the floor.

# Solution 1 - Dynamic Programming (bottom up approach)
# O(n) time complexity
# O(n) space complexity
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


# Solution 2 - Optimized Solution 1
# O(n) time complexity
# O(2) space complexity
def minCostClimbingStairs2(cost):
    """
    :type cost: List[int]
    :rtype: int
    """
    # we keep track only of the last two steps' costs
    accumulated_costs = [0 for _ in range(2)]

    for i in range(len(cost)):
        if i > 1:
            current_cost = cost[i] + min(accumulated_costs[0], accumulated_costs[1])
        else:
            # no previous costs
            current_cost = cost[i]
        # move last cost to first position
        accumulated_costs[0] = accumulated_costs[1]
        # add minimum cost at the current step position 1
        accumulated_costs[1] = current_cost
    # return minimum of the last two steps (we can choose to start from 0 or 1 - first or second step)
    return min(accumulated_costs[0], accumulated_costs[1])


print(minCostClimbingStairs2([10, 15, 20]))
print(minCostClimbingStairs2([1, 100, 1, 1, 1, 100, 1, 1, 100, 1]))
