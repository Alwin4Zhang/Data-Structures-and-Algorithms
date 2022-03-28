

# 单调栈问题
def next_greater_number(nums):
    n = len(nums)
    res = [0] * n
    stack = []
    for i in range(n-1, -1, -1):
        # 如果栈顶元素比当前数字小直接弹出栈顶
        while stack and stack[-1] <= nums[i]:
            stack.pop()
        res[i] = -1 if not stack else stack[-1]
        # 加入新的栈顶
        stack.append(nums[i])
    return res


nums = [2, 1, 2, 4, 3]
res = next_greater_number(nums)
print(res)

# 496.下一个更大元素I


def next_greater_number2(nums1, nums2):
    res = {}
    n = len(nums1)
    stack = []
    # 因为nums1是nums2的子集，所以用nums2构建单调栈
    for i in range(n-1, -1, -1):
        while stack and stack[-1] <= nums2[i]:
            stack.pop()
        res[nums2[i]] = -1 if not stack else stack[-1]
        stack.append(nums2[i])
    # 获取数字对应的后一个大的数字
    return [res[num] for num in nums1]

# 1118 一月有多少天
# 存索引 更方便一些
def daily_temperatures(nums):
    n = len(nums)
    res = [0] * n
    stack = []
    for i in range(n-1, -1, -1):
        while stack and nums[stack[-1]] <= nums[i]:
            stack.pop()
        res[i] = 0 if not stack else (stack[-1] - i)
        stack.append(i)
    return res

T = [73,74,75,71,69,76]
res = daily_temperatures(T)
print(res)