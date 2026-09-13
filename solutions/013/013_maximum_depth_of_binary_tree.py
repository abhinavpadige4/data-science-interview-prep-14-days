class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def max_depth(root):
    """
    Given the root of a binary tree, return its maximum depth.
    A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.
    
    Args:
        root: TreeNode - root of the binary tree
        
    Returns:
        int - maximum depth of the tree
        
    Time Complexity: O(n) - where n is the number of nodes in the tree
    Space Complexity: O(h) - where h is the height of the tree (due to recursion stack)
    """
    if not root:
        return 0
    
    # Recursively find the depth of left and right subtrees
    left_depth = max_depth(root.left)
    right_depth = max_depth(root.right)
    
    # Return the maximum of the two depths plus 1 for the current node
    return max(left_depth, right_depth) + 1


if __name__ == "__main__":
    # Test case 1: [3,9,20,null,null,15,7]
    root1 = TreeNode(3)
    root1.left = TreeNode(9)
    root1.right = TreeNode(20)
    root1.right.left = TreeNode(15)
    root1.right.right = TreeNode(7)
    print(f"Test 1: {max_depth(root1)}")  # Expected: 3
    
    # Test case 2: [1,null,2]
    root2 = TreeNode(1)
    root2.right = TreeNode(2)
    print(f"Test 2: {max_depth(root2)}")  # Expected: 2
    
    # Test case 3: []
    root3 = None
    print(f"Test 3: {max_depth(root3)}")  # Expected: 0