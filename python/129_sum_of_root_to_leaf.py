from icecream import ic

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def insert_tree(arr, root, i, n):
    if i < n:
        temp = TreeNode(arr[i])
        root = temp

        root.left = insert_tree(arr, root.left, 2 * i + 1, n)
        root.right = insert_tree(arr, root.right, 2 * i + 2, n)
    return root

def build_tree(arr):
    if not arr:
        return None
    return insert_tree(arr, None, 0, len(arr))

class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def tree(node, current_sum):
            if not node:
                return 0
            
            current_sum = current_sum * 10 + node.val

            if not node.left and not node.right:
                return current_sum
            
            left_sum = tree(node.left, current_sum)
            right_sum = tree(node.right, current_sum)

            return left_sum + right_sum
        
        return tree(root, 0)

# Example usage
arr = [1, 2, 3]
root = build_tree(arr)
sol = Solution()
ic(sol.sumNumbers(root))  # Output should be 25 (12 + 13)
