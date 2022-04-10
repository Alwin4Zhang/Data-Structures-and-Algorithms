"""
给你输入若干形如 [begin, end] 的区间，代表若干会议的开始时间和结束时间，请你计算至少需要申请多少间会议室。
函数签名如下：
// 返回需要申请的会议室数量
int minMeetingRooms(int[][] meetings);
比如给你输入 meetings = [[0,30],[5,10],[15,20]]，算法应该返回 2，
因为后两个会议和第一个会议时间是冲突的，至少申请两个会议室才能让所有会议顺利进行。
换句话说，如果把每个会议的起始时间看做一个线段区间，那么题目就是让你求最多有几个重叠区间，仅此而已。
"""


def min_meeting_rooms(meetings):
    n = len(meetings)
    begin, end = [0] * n, [0] * n
    # 把左端点和右断点单独拿出来
    for i in range(n):
        begin[i] = meetings[i][0]
        end[i] = meetings[i][1]
    # 排序后就是图中的红点
    begin.sort()
    # 排序后就是图中的绿点
    end.sort()
    # 扫描过程中的计数器
    count = 0
    # 双指针
    res = i = j = 0
    while i < n and j < n:
        if begin[i] < end[j]:
            # 扫描到一个红点
            count += 1
            i += 1
        else:
            # 扫描到一个绿点
            count -= 1
            j += 1
        res = max(res, count)
    return res


meetings = [[0, 30], [5, 10], [15, 20]]
res = min_meeting_rooms(meetings)
print(res)
