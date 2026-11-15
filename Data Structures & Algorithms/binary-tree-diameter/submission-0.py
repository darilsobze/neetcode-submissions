# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        stack = [root]
        visited = {
            None: (0,0)
        }

        while stack:
            node = stack[-1]
            if node.left and not node.left in visited:
                stack.append(node.left)
            elif node.right and not node.right in visited:
                stack.append(node.right)
            else:
                node = stack.pop()
                leftHeight, leftDiameter = visited[node.left]
                rightHeight, rightDiameter = visited[node.right]

                visited[node]= (1+ max(leftHeight, rightHeight), max(leftHeight+rightHeight, leftDiameter, rightDiameter) )

        return visited[root][1]
