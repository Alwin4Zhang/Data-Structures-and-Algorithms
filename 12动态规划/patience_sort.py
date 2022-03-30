def lis(nums):
    n = len(nums)
    top = [0] * n
    piles = 0
    for i in range(n):
        poker = nums[i]
        left, right = 0, piles
        while left < right:
            mid = (left + right) // 2
            if top[mid] > poker:
                right = mid
            elif top[mid] < poker:
                left = mid + 1
            else:
                right = mid
        if left == piles:
            piles += 1
        top[left] = poker
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