def lis(nums):
    n = len(nums)
    # 最坏状态是纸牌正序排列，有多少个纸牌拆多少个堆  top数组用于维护所有堆的堆顶最小点数的纸牌
    top = [0] * n
    piles = 0
    for i in range(n):
        poker = nums[i]
        # left每次都是从0开始，right就是堆的个数，每次的任务就是把当前的poker通过二分查找放进该放的堆中
        left, right = 0, piles
        while left < right:
            mid = (left + right) // 2
            if top[mid] > poker: # 当mid位置的纸牌点数≥poker时，当前的poker放入mid左边的堆
                right = mid
            elif top[mid] < poker: # 放入mid右边的堆
                left = mid + 1
            else:
                right = mid
        if left == piles: # 当左边界和堆的个数相同时，需要新开一个堆
            piles += 1
        top[left] = poker # 更新poker放入的堆顶元素
    return piles


def lis2(nums):
    stack = [[]]
    for v in nums:
        for s in stack:
            if not s or s[-1] >= v:
                s.append(v)
                break
        else:
            stack.append([v])
    return len(stack)

nums = [6,3,4,10,11,2,9,1,13,7,4,8,12]
res = lis(nums)
res2 = lis2(nums)
print(res == res2)