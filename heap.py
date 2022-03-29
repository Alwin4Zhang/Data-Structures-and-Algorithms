# -*- coding: utf-8 -*-

"""
堆排序问题
"""
import heapq

# heapq默认是小顶堆
# TODO:可用于实现priorityQueue类的功能

nums = [1, 3, 2, 5, 4]

# 构建小顶堆
pq = []
for num in nums:
    heapq.heappush(pq, num)

res = []
while pq:
    res.append(heapq.heappop(pq))
print(res)

# 默认是用iterator的索引0作为比较标准
nums = [(1, 'jack'), (3, 'tom'), (2, 'jerry')]
pq = []
for num in nums:
    heapq.heappush(pq, num)
res = []
while pq:
    res.append(heapq.heappop(pq))
print(res)


nums = [1, 3, 2, 5, 4]
# 构建大顶堆
pq = []
for num in nums:
    heapq.heappush(pq, -num)

res = []
while pq:
    res.append(-heapq.heappop(pq))
print(res)


# 自定义排序标准
class State(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __lt__(self, other):  # 小于则是小顶堆，大于则是大顶堆
        return self.y < other.y


a = State(3, 1)
b = State(2, 3)
c = State(2, 2)

pq = []
for n in [a, b, c]:
    heapq.heappush(pq, n)
res = []
while pq:
    cur_state = heapq.heappop(pq)
    res.append((cur_state.x, cur_state.y))
print(res)


# json对象的小顶堆
class State(object):
    def __init__(self, x, field):
        self.x = x
        self.field = field

    def __lt__(self, other):
        if self.field not in self.x or other.field not in other.x:
            return False
        return self.x[self.field] < other.x[other.field]


a = State(x={'age': 18, 'name': 'zs'}, field='age')
b = State({'age': 20, 'name': 'ls'}, 'age')
c = State({'age': 19, 'name': 'ww'}, 'age')

pq = []
for n in [a, b, c]:
    heapq.heappush(pq, n)
res = []
while pq:
    cur_state = heapq.heappop(pq)
    res.append(cur_state.x)
print(res)