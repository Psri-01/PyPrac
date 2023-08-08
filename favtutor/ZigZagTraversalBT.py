class TreeNode:
    def __init__(self,value):
        self.val=value
        self.left=None
        self.right=None
def zigzagTraversal(root):
    if not root:
        return []
    result=[]
    current_level=[root]
    left_to_right=True
    while current_level:
        level_values=[]
        next_level=[]
        for node in current_level:
            level_values.append(node.val)
            if node.left:
                next_level.append(node.left)
            if node.right:
                next_level.append(node.right)
        if not left_to_right:
            level_values.reverse()
        result.extend(level_values)
        left_to_right=not left_to_right
        current_level=next_level
    return result
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)
print(zigzagTraversal(root))
# 1 3 2 4 5 6 7
