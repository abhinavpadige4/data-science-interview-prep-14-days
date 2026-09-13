def intersection(nums1, nums2):
    """
    Given two integer arrays nums1 and nums2, return an array of their intersection.
    Each element in the result must be unique.
    
    Args:
        nums1: List[int] - first array
        nums2: List[int] - second array
        
    Returns:
        List[int] - unique intersection of the two arrays
        
    Time Complexity: O(n + m) - where n and m are lengths of nums1 and nums2
    Space Complexity: O(n + m) - storage for both sets
    """
    # Convert both arrays to sets to remove duplicates and enable O(1) lookup
    set1 = set(nums1)
    set2 = set(nums2)
    
    # Return the intersection of both sets
    return list(set1 & set2)


if __name__ == "__main__":
    # Test case 1
    nums1 = [1, 2, 2, 1]
    nums2 = [2, 2]
    print(f"Test 1: {intersection(nums1, nums2)}")  # Expected: [2]
    
    # Test case 2
    nums1 = [4, 9, 5]
    nums2 = [9, 4, 9, 8, 4]
    print(f"Test 2: {intersection(nums1, nums2)}")  # Expected: [9, 4] or [4, 9]
    
    # Test case 3
    nums1 = [1, 2, 3]
    nums2 = [4, 5, 6]
    print(f"Test 3: {intersection(nums1, nums2)}")  # Expected: []