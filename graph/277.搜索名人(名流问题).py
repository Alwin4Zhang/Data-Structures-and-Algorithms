
"""
名人问题：
条件，所有人都认识他，但是他不认识其他任何一个人。只要认识其他一个人，他就不是名人
"""


def knows(a, b):
    # 返回a是否认识b
    pass


# 暴力解
def find_celebrity(n):
    count = ans = -1
    for cand in range(n):
        for other in range(n):
            if cand == other:
                continue
            if knows(cand, other) or not knows(other, cand):  # cand不是名人
                break
            # else其实就是knows(other,cand)
        if other == n:  # 也就是cand所有人都认识他
            return cand
    # 没有人符合名人特征
    return -1

# 优化解法


def find_celebrity2(n):
    if n == 1:
        return 0
    q = []
    for i in range(n):
        q.append(i)

    while len(q) >= 2:  # 一直排除，最后只剩下一个候选人为止
        cand = q.pop(0)
        other = q.pop(0)
        if knows(cand, other) or not knows(other, cand):  # cand不可能是名人，排除，让other归队首
            q.insert(0, other)
        else:  # other不可能是名人，让cand归队首
            q.insert(0, cand)

    # 现在排除得只剩一个候选人，判断他是否真的是名人
    cand = q.pop(0)
    for other in range(n):
        if other == cand:
            continue
        # 如果other不认识cand或者cand认识其他人，则不满足名人的要求
        if not knows(other, cand) or knows(cand, other):
            return -1
    # cand是名人
    return cand


graph = [
    [1, 1, 0],
    [0, 1, 0],
    [1, 1, 1]
]
