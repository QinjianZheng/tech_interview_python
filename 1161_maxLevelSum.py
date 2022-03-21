from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    @staticmethod
    def maxLevelSum(root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        tree = []
        node_queue = [root]
        while len(node_queue) > 0:
            level_temp = []
            for i in range(0, len(node_queue)):
                node = node_queue.pop(0)
                # print(node.val)
                level_temp.append(node.val)
                if node.left:
                    node_queue.append(node.left)
                if node.right:
                    node_queue.append(node.right)
            tree.append(level_temp)
        max_sum = root.val
        max_level = 1
        for i in range(0, len(tree)):
            level_sum = sum(tree[i])
            if max_sum < level_sum:
                max_sum = level_sum
                max_level = i+1
        # print(tree)
        return max_level


if __name__ == '__main__':
    n5 = TreeNode(-8)
    n4 = TreeNode(7)
    n3 = TreeNode(7, n4, n5)
    n2 = TreeNode(0)
    n1 = TreeNode(1, n2, n3)
    print(Solution.maxLevelSum(n1) == 2)


