def first_uniq_char(s):
    """
    Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.
    
    Args:
        s: str - input string
        
    Returns:
        int - index of the first non-repeating character, or -1 if it does not exist
        
    Time Complexity: O(n) - two passes through the string
    Space Complexity: O(1) - fixed size array for 26 lowercase English letters
    """
    if not s:
        return -1
    
    # Count frequency of each character
    count = [0] * 26  # Assuming lowercase English letters only
    
    for char in s:
        count[ord(char) - ord('a')] += 1
    
    # Find the first character with frequency 1
    for i, char in enumerate(s):
        if count[ord(char) - ord('a')] == 1:
            return i
    
    return -1


if __name__ == "__main__":
    # Test case 1
    s1 = "leetcode"
    print(f"Test 1: {first_uniq_char(s1)}")  # Expected: 0
    
    # Test case 2
    s2 = "loveleetcode"
    print(f"Test 2: {first_uniq_char(s2)}")  # Expected: 2
    
    # Test case 3
    s3 = "aabb"
    print(f"Test 3: {first_uniq_char(s3)}")  # Expected: -1