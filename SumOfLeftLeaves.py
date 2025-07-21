#!/usr/bin/env python

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = self.right = None

def input_binary_tree():
    input_values = input().split()
    index = 0
    num_nodes = int(input_values[index])
    index += 1
    if (num_nodes == 0):
        return None
        
    nodes = []
    current_parent_index = 0
    
    root = TreeNode(int(input_values[index]))
    index += 1
    nodes.append(root)
    
    for i in range(1, num_nodes, 2):
        left_val = int(input_values[index])
        index += 1
        if (left_val != -1):
            left = TreeNode(left_val)
            nodes.append(left)
            nodes[current_parent_index].left = left
        
        right_val = int(input_values[index])
        index += 1
        if (right_val != -1):
            right = TreeNode(right_val)
            nodes.append(right)
            nodes[current_parent_index].right = right
        
        current_parent_index += 1
        
    return root
"""
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = self.right = None
"""
def isLeaf(node):
    if node is None:
        return False
    if node.left is None and node.right is None:
        return True
    return False
def sum_of_left_leaves(root):
    """
    Write your code here
    :type root: TreeNode
    :rtype: int
    """
    res=0
    if root is not None:
        if isLeaf(root.left):
            res+=root.left.val
        else:
            res+=sum_of_left_leaves(root.left)
        res+=sum_of_left_leaves(root.right)
    return res
root = input_binary_tree()
sum = sum_of_left_leaves(root)

print(sum)
