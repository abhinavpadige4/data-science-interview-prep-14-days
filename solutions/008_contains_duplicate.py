def contains_duplicate(nums):
    """
    Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.
    
    Args:
        nums: List[int] - list of integers
        
    Returns:
        bool - True if any value appears at least twice, False otherwise
        
    Time Complexity: O(n) - single pass through the array
    Space Complexity: O(n) - hash set storage
    """
    seen = set()
    for num in nums:
        if num in seen:
            return True
        seen.add(num)
    return False


if __name__ == "__main__":
    # Test case 1
    nums1 = [1, 2, 3, 1]
    print(f"Test 1: {contains_duplicate(nums1)}")  # Expected: True
    
    # Test case 2
    nums2 = [1, 2, 3, 4]
    print(f"Test 2: {contains_duplicate(nums2)}")  # Expected: False
    
    # Test case 3
    nums3 = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]
    print(f"Test 3: {contains_duplicate(nums3)}")  # Expected: True