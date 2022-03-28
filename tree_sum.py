# -*- coding: utf-8 -*-
'''
    @Time    : 2022/3/10 10:13 上午
    @Author  : alwin
    @Email   : alwin114@hotmail.com
'''


class TreeNode:
    def __init__(self, left=None, right=None, val=0):
        self.left = left
        self.right = right
        self.val = val


def tree_sum(root):
    if not root:
        return 0
    return tree_sum(root.left) + root.val + tree_sum(root.right)


a = TreeNode(val=1)
b = TreeNode(val=2)
c = TreeNode(val=3)
d = TreeNode(val=4)
e = TreeNode(val=5)

a.left = b
a.right = c
b.left = d
c.right = e

sum = tree_sum(c)
print(sum)
