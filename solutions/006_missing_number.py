def missing_number(nums):
    """
    Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.
    
    Args:
        nums: List[int] - list of n distinct numbers in range [0, n]
        
    Returns:
        int - the missing number
        
    Time Complexity: O(n) - single pass through the array
    Space Complexity: O(1) - constant extra space
    """
    n = len(nums)
    # Expected sum of numbers from 0 to n
    expected_sum = n * (n + 1) // 2
    # Actual sum of numbers in the array
    actual_sum = sum(nums)
    # The difference is the missing number
    return expected_sum - actual_sum


if __name__ == "__main__":
    # Test case 1
    nums1 = [3, 0, 1]
    print(f"Test 1: {missing_number(nums1)}")  # Expected: 2
    
    # Test case 2
    nums2 = [0, 1]
    print(f"Test 2: {missing_number(nums2)}")  # Expected: 2
    
    # Test case 3
    nums3 = [9, 6, 4, 2, 3, 5, 7, 0, 1]
    print(f"Test 3: {missing_number(nums3)}")  # Expected: 8