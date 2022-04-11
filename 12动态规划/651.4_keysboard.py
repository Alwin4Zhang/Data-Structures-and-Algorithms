"""
假设你有一个特殊的键盘，上面只有四个键，它们分别是：

1、A 键：在屏幕上打印一个 A。

2、Ctrl-A 键：选中整个屏幕。

3、Ctrl-C 键：复制选中的区域到缓冲区。

4、Ctrl-V 键：将缓冲区的内容输入到光标所在的屏幕上。

这就和我们平时使用的全选复制粘贴功能完全相同嘛，只不过题目把 Ctrl 的组合键视为了一个键。现在要求你只能进行 N 次操作，请你计算屏幕上最多能显示多少个 A？

函数签名如下：

int maxA(int N);
比如说输入 N = 3，算法返回 3，因为连按 3 次 A 键是最优的方案。

如果输入是 N = 7，则算法返回 9，最优的操作序列如下：

A, A, A, Ctrl-A, Ctrl-C, Ctrl-V, Ctrl-V
可以得到 9 个 A。


思路：动态规划
【状态】定义3个状态，1.N为输入次数 2.当前A的个数a_num 3.剪贴板上A的个数为copy
【选择】(1) A  (2) Ctrl-A (3) Ctrl-C  (4) Ctrl-V  但是Ctrl-A和Ctrl-C一般都是成对出现的

分解问题：
dp(n-1,a_num+1,copy) # 选择按下A  解释：按下A，消耗一次输入次数，a的总个数加一
dp(n-1,a_num+copy,copy) # 选择按下Ctrl-V  解释：按下ctrl-V  消耗一次输入次数，a的总个数加剪贴板上的copy个数
dp(n-2,a_num,a_num) # 安装ctrl-A + ctrl-C  解释：剪切板中 A 的数量变为屏幕上 A 的数量，同时消耗 2 个操作数

当然也会存在ctrl-A之后不用ctrl-C


解题思路：https://labuladong.github.io/algo/3/27/93/
"""


def maxA(n):
    # 对于 (n, a_num, copy) 这个状态，
    # 屏幕上能最终最多能有 dp(n, a_num, copy) 个 A

    # 1.时间复杂度是o(n^3) 比较高，大概率是无法通过验证
    # memo = {}

    # def dp(n, a_num, copy):
    #     # base case
    #     if n <= 0:
    #         return a_num
    #     # 重叠子问题
    #     if (n, a_num, copy) in memo:
    #         return memo[(n, a_num, copy)]
    #     res = max(
    #         dp(n-1, a_num+1, copy),
    #         dp(n-1, a_num+copy, copy),
    #         dp(n-2, a_num, a_num)
    #     )
    #     memo[(n, a_num, copy)] = res
    #     return memo[(n, a_num, copy)]
    # return dp(n, 0, 0)
    """
    这个算法基于这样一个事实，最优按键序列一定只有两种情况：
    要么一直按 A：A,A,…A（当 N 比较小时）。
    要么是这么一个形式：A,A,…C-A,C-C,C-V,C-V,…C-V（当 N 比较大时）。
    时间复杂度为O(n^2)
    """
    dp = [0] * (n+1)
    for i in range(1, n):
        # 按A键
        dp[i] = dp[i-1] + 1
        for j in range(2, i):
            # i为当前要处理的位置，倒序递归，j为ctrl-V其实的位置；那么 j 之前的 2 个操作就应该是 C-A C-C 了：
            # 全选 & 复制 dp[j-2]，连续粘贴 i - j 次
            # 屏幕上共 dp[j - 2] * (i - j + 1) 个 A
            dp[i] = max(dp[i], dp[j-2] * (i-j+1))
    return dp[-1]
