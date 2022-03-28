from collections import defaultdict


def canFinish(numCourses, prerequisites):
    graph = defaultdict(list)
    # 构图
    for pair in prerequisites:
        graph[pair[1]].append(pair[0])
    # 构建入度数组
    indegrees = [0] * numCourses
    for pair in prerequisites:
        indegrees[pair[0]] += 1

    # 添加没有入度的节点作为根节点开始遍历
    queue = []
    for i in range(numCourses):
        if indegrees[i] == 0:
            queue.append(i)
    count = 0
    while queue:
        cur = queue.pop(0)
        count += 1
        for v in graph[cur]:
            # 遍历一次，入度-1
            indegrees[v] -= 1
            if indegrees[v] == 0:
                # 如果入度为0，说明v依赖的节点都已经被遍历完
                queue.append(v)
    # 如果所有节点都被遍历过，说明不成环
    return count == numCourses

# 拓扑排序


def topological_sort(numCourses, prerequisites):
    graph = defaultdict(list)
    # 构图
    for pair in prerequisites:
        graph[pair[1]].append(pair[0])
    # 构建入度数组
    indegrees = [0] * numCourses
    for pair in prerequisites:
        indegrees[pair[0]] += 1

    # 添加没有入度的节点作为根节点开始遍历
    queue = []
    for i in range(numCourses):
        if indegrees[i] == 0:
            queue.append(i)
    count = 0
    res = [0] * numCourses
    while queue:
        cur = queue.pop(0)
        res[count] = cur
        count += 1
        for v in graph[cur]:
            # 遍历一次，入度-1
            indegrees[v] -= 1
            if indegrees[v] == 0:
                # 如果入度为0，说明v依赖的节点都已经被遍历完
                queue.append(v)
    # 如果所有节点都被遍历过，说明不成环
    if count != numCourses:
        return []
    return res


numCourses = 4
prerequisites = [[1, 0], [2, 0], [3, 1], [3, 2]]

res = canFinish(numCourses, prerequisites)
print(res)
res = topological_sort(numCourses,prerequisites)
print(res)