# -*- coding: utf-8 -*-
'''
    @Time    : 2022/3/10 3:00 下午
    @Author  : alwin
    @Email   : alwin114@hotmail.com
'''


class TreeNode(object):
    def __init__(self, left=None, right=None, val=0):
        self.left = left
        self.right = right
        self.val = val


def serialized(root):
    '''层序遍历'''
    queue = [root]
    res = [str(root.val)]
    while queue:
        size = len(queue)
        for i in range(size):
            cur_node = queue.pop(0)
            if cur_node.left:
                queue.append(cur_node.left)
                res.append(str(cur_node.left.val))
            else:
                res.append("#")
            if cur_node.right:
                queue.append(cur_node.right)
                res.append(str(cur_node.right.val))
            else:
                res.append("#")
    return ','.join(res)


def deserialize(data):
    if not data:
        return
    nodes = data.split(',')
    root = TreeNode(val=int(nodes[0]))
    queue = [root]
    nodes.pop(0)
    # for i in range(1, len(nodes)):
    while queue:
        cur_node = queue.pop(0)
        left = nodes.pop(0)
        if left != "#":
            cur_node.left = TreeNode(val=int(left))
            queue.append(cur_node.left)
        right = nodes.pop(0)
        if right != "#":
            cur_node.right = TreeNode(val=int(right))
            queue.append(cur_node.right)

    return root


count = 0


def count_nodes(root):  # 统计有多少个节点
    def traverse(root):
        if not root:
            return
        global count
        count += 1
        traverse(root.left)
        traverse(root.right)

    traverse(root)
    return count


a = TreeNode(val=1)
b = TreeNode(val=2)
c = TreeNode(val=3)
d = TreeNode(val=4)
e = TreeNode(val=5)
a.left = b
a.right = c
b.right = d
d.left = e

seri_tree = serialized(a)

root = deserialize(seri_tree)

ct = count_nodes(a)
print(ct)