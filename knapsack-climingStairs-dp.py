"""
Author: Xiaolou Huang
"""


# prefixes method Dynamic programming for 0-1 Knapsack problem
# param lst, include a list of tuples in (w, v) format, where w is the weight, and v is the value
# expected table for input [(1, 3), (2, 4), (3, 5), (4, 8)]:
#   [0, 0, 0, 0, 0]
#   [0, 3, 3, 3, 3]
#   [0, 3, 4, 4, 4]
#   [0, 3, 7, 7, 7]
#   [0, 3, 7, 8, 8]
#   [0, 3, 7, 9, 11]
#   [0, 3, 7, 12, 12]
def knapsack(lst, maxW):
    n = len(lst)
    table = [[0 for i in range(n + 1)] for j in range(maxW + 1)]  # init the table
    for col in range(1, n + 1):  # column for items
        for row in range(1, maxW + 1):  # row for weights
            if row < lst[col - 1][0]:  # if current capacity is smaller than the weight of the item, copy previous value
                table[row][col] = table[row][col - 1]
            else:  # if current capacity is greater than the weight of the item
                # compare the value on the left and the current item value + previous table value
                table[row][col] = max(table[row][col - 1], table[row - lst[col - 1][0]][col - 1] + lst[col - 1][1])
    # print the table
    for row in range(maxW + 1):
        print(table[row])


# Find how many ways to climb a given stairs. Traditional way.
# @param n, number of stairs need to climb
def climb_staircase(n):
    if n < 0:
        return 0
    if n == 0:
        return 1
    return climb_staircase(n - 1) + climb_staircase(n - 2) + climb_staircase(n - 3)


# Find how many ways to climb a given stairs. DP with memorization.
# @param n, number of stairs need to climb
memo = {}  # memorization table, using dictionary
def climb_staircase(n):
    if n in memo:
        return memo[n]
    if n < 0:  # if the steps exceed the remaining stairs left, don't count as a solution
        return 0
    if n == 0:  # if the steps exactly equal to the remaining stairs left, count as a solution
        return 1
    memo[n] = climb_staircase(n - 1) + climb_staircase(n - 2) + climb_staircase(n - 3)
    return memo[n]


# Find the size of the smallest set of unit-length closed intervals that contains all of the given points.
# @param points, the list contains all the points
def find_smallest_set_unit_length(points):
    points.sort()  # sort the points first, using Timsort time complexity is O(nlogn)
    print(points)
    s = []  # the final set
    subset = []  # subsets in the final set
    interval = points[0] + 1  # the interval to check if the number is within
    while points:
        if points[0] <= interval:
            if len(points) == 1:  # if it's last item, add the number into subset and add the subset to the final set 's'
                subset.append(points[0])
                points.remove(points[0])
                s.append(subset)
                subset = []
            else:
                subset.append(points[0])
                points.remove(points[0])
        else:  # add the number into subset and put subset into the final set 's'
            s.append(subset)
            subset = []
            interval = points[0] + 1
    print('Size: ', len(s))


def main():
    lst = [(1, 3), (2, 4), (3, 5), (4, 8)]
    lst1 = [(10, 60), (20, 100), (30, 120)]
    knapsack(lst, 6)
    # ===================
    x = climb_staircase(3)
    print('Number of stairs: 3')
    print('Number of ways: ', x)
    x = climb_staircase(4)
    print('Number of stairs: 4')
    print('Number of ways: ', x)
    x = climb_staircase(5)
    print('Number of stairs: 5')
    print('Number of ways: ', x)
    # ====================
    points = [0.8, 4.3, 1.7, 5.4]
    points1 = [0.8, 2.3, 3.1, 1.7, 3.6, 4.0, 4.2, 5.5, 5.2, 1.0, 3.9, 4.7]
    find_smallest_set_unit_length(points1)


if __name__ == '__main__':
    main()
