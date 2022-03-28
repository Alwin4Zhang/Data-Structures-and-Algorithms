# -*- coding: utf-8 -*-
'''
  @CreateTime	:  2022/03/28 11:31:25
  @Author	:  Alwin Zhang
  @Mail	:  zjfeng@homaytech.com
'''

# 最小生成树问题    并查集(Union Find)算法构建树
import heapq
import collections


class UnionFind(object):
    def __init__(self, n):
        # 初始化节点是自动指向自己
        self.parent = list(range(n))

    def find(self, x):
        while self.parent[x] != x:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x

    def union(self, x1, x2):
        self.parent[self.find(x1)] = self.find(x2)

    def connected(self, x1, x2):
        return self.find(x1) == self.find(x2)


# 城市的编号是从1-n
n = 3
connections = [[1, 2, 5], [1, 3, 6], [2, 3, 1]]


def minimumCost(n, connections):
    uf = UnionFind(n+1)
    mst = 0
    # 按照边的权重排序,贪心算法,从最小权重开始构建树
    connections = sorted(connections, key=lambda x: x[-1])

    count = n
    for edge in connections:
        u, v, weight = edge
        if uf.connected(u, v):
            continue
        mst += weight
        uf.union(u, v)
        count -= 1
    return mst if count == 1 else -1


res = minimumCost(n, connections)
print(res)


# BFS和visited数组方式实现最小生成树（MST）


def prim(n, connections):
    # 将s的横切边加入优先队列

    def build_graph(n, connections):
        # 图中一共有几个节点
        graph = collections.defaultdict(list)
        for conn in connections:
            u, v, weight = conn
            # 无向图就相当于双向图
            graph[u].append((u, v, weight))
            graph[v].append((v, u, weight))
        return graph
        
    def cut(s):
        # 遍历s的临邻边
        for edge in graph[s]:
            _from, _to, weight = edge
            if in_mst[_to]:
                # 节点to已经在MST中，其实就是from->to 已经在s节点的横切边中，跳过
                continue
            # 将和s没有交集的横切边加入横切边队列
            heapq.heappush(pq, (weight, _from, _to))

    graph = build_graph(n, connections)
    # 小顶堆
    pq = []
    # 用于记录节点是否在MST中 因为节点索引从1开始，所以最终除了0索引是False，其他所有都是True
    in_mst = [False] * (n + 1)
    # 记录最小生成树的权重和
    weight_sum = 0
    # 随便从一个点开始切分都可以，我们不妨从节点0开始
    in_mst[1] = True
    cut(1)

    # 不断进行切分，向最小生成树中添加边
    while pq:
        weight, _from, _to = heapq.heappop(pq)
        if in_mst[_to]:
            continue
        weight_sum += weight
        in_mst[_to] = True
        cut(_to)
    return weight_sum


prim(n, connections)
