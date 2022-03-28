"""
给你输入一个包含n个节点的图，用一个正数n和一个数组edges表示，
其中edges[i] = [ai,bi]表示图中节点ai和bi之间有一条边。请你计算这幅图的连通分量个数
"""
import collections


class UF(object):
    count = 0
    parent = [0] * n
    def union_find(n):
        nonlocal count
        count = n
        parent = [0] * n
        for i in range(n):
            parent[i] = i

    def union(p, q):
        nonlocal count
        root_p = find(p)
        root_q = find(q)
        if root_p == root_q:
            return
        parent[root_q] = root_p
        count -= 1

    def connected(p, q):
        # 判断是否连通，就是找根节点是否相同
        root_p = find(p)
        root_q = find(q)
        return root_p == root_q

    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x
