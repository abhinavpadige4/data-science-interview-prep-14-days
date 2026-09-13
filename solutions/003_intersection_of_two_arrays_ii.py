def intersect(nums1, nums2):
    """
    Given two integer arrays nums1 and nums2, return an array of their intersection.
    Each element in the result must appear as many times as it shows in both arrays.
    
    Args:
        nums1: List[int] - first array
        nums2: List[int] - second array
        
    Returns:
        List[int] - intersection of the two arrays with proper frequencies
        
    Time Complexity: O(n + m) - where n and m are lengths of nums1 and nums2
    Space Complexity: O(min(n, m)) - hash map for the smaller array
    """
    # Use the smaller array to build the frequency map for better space complexity
    if len(nums1) > len(nums2):
        nums1, nums2 = nums2, nums1
    
    # Build frequency map for nums1
    freq_map = {}
    for num in nums1:
        freq_map[num] = freq_map.get(num, 0) + 1
    
    # Find intersection
    result = []
    for num in nums2:
        if num in freq_map and freq_map[num] > 0:
            result.append(num)
            freq_map[num] -= 1
    
    return result


if __name__ == "__main__":
    # Test case 1
    nums1 = [1, 2, 2, 1]
    nums2 = [2, 2]
    print(f"Test 1: {intersect(nums1, nums2)}")  # Expected: [2, 2]
    
    # Test case 2
    nums1 = [4, 9, 5]
    nums2 = [9, 4, 9, 8, 4]
    print(f"Test 2: {intersect(nums1, nums2)}")  # Expected: [4, 9] or [9, 4]
    
    # Test case 3
    nums1 = [1, 2, 2, 1]
    nums2 = [2]
    print(f"Test 3: {intersect(nums1, nums2)}")  # Expected: [2]