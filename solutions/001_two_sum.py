def two_sum(nums, target):
    """
    Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
    
    Args:
        nums: List[int] - list of integers
        target: int - target sum
        
    Returns:
        List[int] - indices of the two numbers that add up to target
        
    Time Complexity: O(n) - single pass through the array
    Space Complexity: O(n) - hash map storage
    """
    num_map = {}  # value -> index
    
    for i, num in enumerate(nums):
        complement = target - num
        if complement in num_map:
            return [num_map[complement], i]
        num_map[num] = i
    
    return []  # No solution found


if __name__ == "__main__":
    # Test case 1
    nums1 = [2, 7, 11, 15]
    target1 = 9
    print(f"Test 1: {two_sum(nums1, target1)}")  # Expected: [0, 1]
    
    # Test case 2
    nums2 = [3, 2, 4]
    target2 = 6
    print(f"Test 2: {two_sum(nums2, target2)}")  # Expected: [1, 2]
    
    # Test case 3
    nums3 = [3, 3]
    target3 = 6
    print(f"Test 3: {two_sum(nums3, target3)}")  # Expected: [0, 1]