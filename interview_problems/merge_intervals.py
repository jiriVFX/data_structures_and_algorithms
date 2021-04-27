# https://leetcode.com/problems/merge-intervals/
# Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals,
# and return an array of the non-overlapping intervals that cover all the intervals in the input.

# Solution 1 - Brute force (compare intervals against each other)
# O(n^2) time complexity, O(n) space complexity - Time limit exceeded on LeetCode
def merge(intervals):
    """
    :type intervals: List[List[int]]
    :rtype: List[List[int]]
    """
    for i in range(len(intervals)):
        # if item at position i is None, continue to the next one
        if intervals[i] is None:
            continue
        start_i = intervals[i][0]
        end_i = intervals[i][1]

        for j in range(i + 1, len(intervals)):
            # if item at position j is None, continue to the next one
            if intervals[j] is None:
                continue

            start_j = intervals[j][0]
            end_j = intervals[j][1]
            # if there is an overlap between the two intervals
            if (start_j <= start_i <= end_j) or (start_j <= end_i <= end_j) or (start_j > start_i and end_j < end_i):
                # make sure the merged interval starts with smallest start
                # and largest end number of the two intervals
                if start_i > start_j:
                    start_i = start_j
                if end_i > end_j:
                    end_j = end_i
                # instead of deleting i, which is inefficient (potentially O(n)) using a list,
                # replace it with None (O(1))
                intervals[i] = None
                # replace the j interval with merged interval
                # so other intervals will get checked against the merged interval
                # if we would replace intervals[i],
                # it wouldn't work for cases when e.g. [1, 10] is at the end of the list
                intervals[j] = [start_i, end_j]
            # print(intervals)

    # return items from intervals, that are not None
    return [interval for interval in intervals if interval is not None]


# print(merge([[1, 3], [2, 6], [8, 10], [15, 18]]))
# print(merge([[1, 3], [2, 6], [3, 4], [0, 18]]))
# print(merge([[1, 4], [4, 5]]))
# print(merge([[1, 4], [2, 3]]))
# print(merge([[2, 3], [4, 5], [6, 7], [8, 9], [1, 10]]))


# Solution 2 - sorting - LeetCode solution
# O(n log n) time complexity, O(n) space complexity
def merge_2(intervals):
    """
    :type intervals: List[List[int]]
    :rtype: List[List[int]]
    """
    # sort the list of intervals based on the start (index 0) of each interval
    intervals.sort(key=lambda x: x[0])
    # print(intervals)

    # add the first interval
    merged_intervals = [intervals[0]]

    for i in range(len(intervals)):
        # if previously added interval end is lower than current interval's start
        # the intervals are not overlapping
        if merged_intervals[len(merged_intervals) - 1][1] < intervals[i][0]:
            merged_intervals.append(intervals[i])
        else:
            # if the two overlap, merge their end values
            # we don't need to merge start values as they are sorted
            # => the start is either same or already added interval's start is smaller
            current_end = intervals[i][1]
            previous_end = merged_intervals[len(merged_intervals) - 1][1]
            merged_intervals[len(merged_intervals) - 1][1] = max(current_end, previous_end)

    return merged_intervals


print(merge_2([[1, 3], [2, 6], [8, 10], [15, 18]]))
print(merge_2([[1, 3], [2, 6], [3, 4], [0, 18]]))
print(merge_2([[1, 4], [4, 5]]))
print(merge_2([[1, 4], [2, 3]]))
print(merge_2([[2, 3], [4, 5], [6, 7], [8, 9], [1, 10]]))
