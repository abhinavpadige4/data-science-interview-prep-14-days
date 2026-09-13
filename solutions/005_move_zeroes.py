def move_zeroes(nums):
    """
    Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.
    Note that you must do this in-place without making a copy of the array.
    
    Args:
        nums: List[int] - list of integers to modify in-place
        
    Returns:
        None - modifies nums in-place
        
    Time Complexity: O(n) - single pass through the array
    Space Complexity: O(1) - constant extra space
    """
    # Two-pointer approach: slow pointer for position to place next non-zero
    slow = 0
    
    # Fast pointer scans through the array
    for fast in range(len(nums)):
        if nums[fast] != 0:
            # Swap non-zero element to the slow pointer position
            nums[slow], nums[fast] = nums[fast], nums[slow]
            slow += 1


if __name__ == "__main__":
    # Test case 1
    nums1 = [0, 1, 0, 3, 12]
    move_zeroes(nums1)
    print(f"Test 1: {nums1}")  # Expected: [1, 3, 12, 0, 0]
    
    # Test case 2
    nums2 = [0]
    move_zeroes(nums2)
    print(f"Test 2: {nums2}")  # Expected: [0]
    
    # Test case 3
    nums3 = [1, 2, 3, 0, 0, 0, 4]
    move_zeroes(nums3)
    print(f"Test 3: {nums3}")  # Expected: [1, 2, 3, 4, 0, 0, 0]