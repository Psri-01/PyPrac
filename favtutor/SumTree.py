class TreeNode:
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None
def isSumTree(root):
    if not root:
        return True
    if root.left is None and root.right is None:
        return True
    if isSumTree(root.left) and isSumTree(root.right):
        left_val = root.left.val if root.left else 0
        right_val = root.right.val if root.right else 0
        return root.val == left_val + right_val
    return False
# Construct a sum tree
root = TreeNode(10)
root.left = TreeNode(3)
root.right = TreeNode(7)
root.left.left = TreeNode(1)
root.left.right = TreeNode(2)
root.right.left = TreeNode(4)
root.right.right = TreeNode(3)
if isSumTree(root):
    print("The binary tree is a sum tree")
else:
    print("The binary tree is not a sum tree")
