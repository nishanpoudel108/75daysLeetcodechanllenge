class Solution(object):
    def insert(self, intervals, newInterval):
        res = []

        for interval in intervals:
            # Current interval is completely before newInterval
            if interval[1] < newInterval[0]:
                res.append(interval)

            # Current interval is completely after newInterval
            elif interval[0] > newInterval[1]:
                res.append(newInterval)
                newInterval = interval

            # Overlapping intervals
            else:
                newInterval[0] = min(newInterval[0], interval[0])
                newInterval[1] = max(newInterval[1], interval[1])

        res.append(newInterval)
        return res