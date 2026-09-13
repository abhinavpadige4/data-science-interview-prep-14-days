class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def inorder_traversal(root):
    """
    Given the root of a binary tree, return the inorder traversal of its nodes' values.
    
    Args:
        root: TreeNode - root of the binary tree
        
    Returns:
        List[int] - inorder traversal of the tree's values
        
    Time Complexity: O(n) - where n is the number of nodes in the tree
    Space Complexity: O(n) - due to recursion stack or explicit stack
    """
    result = []
    stack = []
    current = root
    
    while current or stack:
        # Reach the leftmost node of the current node
        while current:
            stack.append(current)
            current = current.left
        
        # Current must be None at this point
        current = stack.pop()
        result.append(current.val)
        
        # We have visited the node and its left subtree.
        # Now, it's right subtree's turn
        current = current.right
    
    return result


if __name__ == "__main__":
    # Test case 1: [1,null,2,3]
    root1 = TreeNode(1)
    root1.right = TreeNode(2)
    root1.right.left = TreeNode(3)
    print(f"Test 1: {inorder_traversal(root1)}")  # Expected: [1, 3, 2]
    
    # Test case 2: []
    root2 = None
    print(f"Test 2: {inorder_traversal(root2)}")  # Expected: []
    
    # Test case 3: [1]
    root3 = TreeNode(1)
    print(f"Test 3: {inorder_traversal(root3)}")  # Expected: [1]