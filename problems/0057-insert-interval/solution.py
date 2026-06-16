#
# @lc app=leetcode id=57 lang=python3
#
# [57] Insert Interval
# Link to youtube video
# https://www.youtube.com/watch?v=A8NUOmlwOlM&t=40s
#

# Test Case #1
# new interval just extends the first interval in list.
intervals = [[1, 3], [6, 9]]
newInterval = [2, 5]
output = [[1, 5], [6, 9]]

# Test Case #2
# new interval extends second interval in list and replaces the 3 inner intervals
intervals = [[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]]
newInterval = [4, 8]
output = [[1, 2], [3, 10], [12, 16]]

# Test Case #3
# new interval is placed at beginning of interval list
intervals = [[3, 5], [6, 7], [8, 10], [12, 16]]
newInterval = [1, 2]
output = [[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]]

# Test Case #4
# new interval is placed at the end of the interval list
intervals = [[3, 5], [6, 7], [8, 10], [12, 16]]
newInterval = [20, 21]
output = [[3, 5], [6, 7], [8, 10], [12, 16], [20, 21]]

# Test Case #5
# new interval is added in between 1st and 2nd intervals. no replacements.
intervals = [[1, 2], [8, 10]]
newInterval = [4, 5]
output = [[1, 2], [4, 5], [8, 10]]


# @lc code=start
class Solution:
    def insert(self, intervals, newInterval):

        # response variable
        res = []

        # iterate through all intervals...
        for i in range(len(intervals)):

            # check if new interval's end value is less than current interval's start value
            if newInterval[1] < intervals[i][0]:
                # if yes... add the new interval BEFORE the next interval and return all the other intervals.
                res.append(newInterval)
                return res + intervals[i:]

            # check if new interval's start value is greater than current interval's end value.
            elif newInterval[0] > intervals[i][1]:
                # if yes... add current interval to res and move to next interval
                res.append(intervals[i])

            # overlapping intervals!
            # if neither of the above cases are true, that means our newInterval is overlapping with our current interval.
            else:
                # we have to redefine the newInterval
                # combine the minimum start value of the two, with the maximum end value of the two
                newInterval = [min(newInterval[0], intervals[i][0]), max(
                    newInterval[1], intervals[i][1])]
                # should we add this new interval to res?
                # NO! there is a chance that this newInterval could then merge with the next interval in the iteration.

        # arriving at this point means your newInterval has never been added to the res.
        # your new interval start value must be greater than any end value in the intervals.
        # add the new interval and return.
        res.append(newInterval)

        return res

# @lc code=end
