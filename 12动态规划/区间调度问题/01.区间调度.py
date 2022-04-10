"""
给定一个区间的集合 intervals ，其中 intervals[i] = [starti, endi] 。返回 需要移除区间的最小数量，使剩余区间互不重叠 。
示例 1:
输入: intervals = [[1,2],[2,3],[3,4],[1,3]]
输出: 1
解释: 移除 [1,3] 后，剩下的区间没有重叠。
"""

def interval_scheduling(intervals):
    intervals = sorted(intervals, key=lambda x: x[1])
    count = 1
    x_end = intervals[0][1]
    for interval in intervals:
        start, end = interval
        if start >= x_end:
            count += 1
            x_end = end
    return count




intvs = [[1, 2], [2, 3], [3, 4], [1, 3]]
count = interval_scheduling(intvs)
print(count)
