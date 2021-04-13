"""
https://leetcode.com/explore/challenge/card/march-leetcoding-challenge-2021/589/week-2-march-8th-march-14th/3666/
"""
import unittest


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        return str(tree_to_list(self))


def tree_to_list(root):
    result = []

    nodes_to_work_with = [root]

    def process_next_node():
        current_node = nodes_to_work_with.pop(0)

        if current_node:
            result.append(current_node.val)
            if not current_node.left and current_node.right:
                nodes_to_work_with.append(TreeNode(None))
            else:
                nodes_to_work_with.append(current_node.left)

            if not current_node.right and current_node.left:
                nodes_to_work_with.append(TreeNode(None))
            else:
                nodes_to_work_with.append(current_node.right)

    process_next_node()

    while nodes_to_work_with:
        # left node
        process_next_node()

        # right_node
        process_next_node()

    return result


class Solution(object):
    def addOneRow(self, root, val, depth):
        """
        :type root: TreeNode
        :type val: int
        :type depth: int
        :rtype: TreeNode
        """

        if depth == 1:
            return TreeNode(val, root)
        else:
            self.insert_row(root, val, depth)
        return root

    def insert_row_recursive(self, root, value, depth):
        if depth == 2:
            left, right = root.left, root.right

            new_left_node = TreeNode(value, left)
            new_right_node = TreeNode(value, right=right)

            root.left, root.right = new_left_node, new_right_node
            return root
        elif depth > 2:
            if root.left:
                self.insert_row_recursive(root.left, value, depth - 1)
            if root.right:
                self.insert_row_recursive(root.right, value, depth - 1)
        elif depth < 2:
            return root

    class Node:
        def __init__(self, node, depth):
            self.node = node
            self.depth = depth

    def insert_row(self, root, value, depth):
        nodes_to_work_on = [Solution.Node(root, 1)]
        required_depth_nodes = []  # list of TreeNodes

        while nodes_to_work_on:
            n = nodes_to_work_on.pop(0)

            left, right = n.node.left, n.node.right

            if n.depth == depth - 1:
                required_depth_nodes.append(n.node)
            else:
                if left:
                    nodes_to_work_on.append(self.Node(left, n.depth + 1))
                if right:
                    nodes_to_work_on.append(self.Node(right, n.depth + 1))

        for node in required_depth_nodes:
            left, right = node.left, node.right

            new_left_node = TreeNode(value, left)
            new_right_node = TreeNode(value, right=right)

            node.left, node.right = new_left_node, new_right_node


class SolutionTestCase(unittest.TestCase):
    def test_ok(self):
        tree = TreeNode(
            4,
            TreeNode(2, TreeNode(3), TreeNode(1)),
            TreeNode(6, left=TreeNode(5)),
        )
        res = Solution().insert_row_recursive(tree, 1, 2)
        self.assertEqual(tree_to_list(res), [4, 1, 1, 2, None, None, 6, 3, 1, 5, None])

    def test_tree_to_list_1(self):
        tree = TreeNode(
            4,
            TreeNode(
                2, TreeNode(3), TreeNode(1)
            ),
            TreeNode(6, left=TreeNode(5)),
        )

        self.assertEqual(tree_to_list(tree), [4, 2, 6, 3, 1, 5, None])

    def test_tree_to_list_2(self):
        tree = TreeNode(
            4, TreeNode(
                2, TreeNode(3), TreeNode(1)
            )
        )
        self.assertEqual(tree_to_list(tree), [4, 2, None, 3, 1])
