def is_anagram(s, t):
    """
    Given two strings s and t, return true if t is an anagram of s, and false otherwise.
    
    Args:
        s: str - first string
        t: str - second string
        
    Returns:
        bool - True if t is an anagram of s, False otherwise
        
    Time Complexity: O(n) - where n is the length of the strings
    Space Complexity: O(1) - since we only store counts for 26 lowercase English letters
    """
    if len(s) != len(t):
        return False
    
    # Count frequency of each character in s
    count = [0] * 26  # Assuming lowercase English letters only
    
    for char in s:
        count[ord(char) - ord('a')] += 1
    
    # Decrease frequency for each character in t
    for char in t:
        index = ord(char) - ord('a')
        count[index] -= 1
        if count[index] < 0:
            return False
    
    return True


if __name__ == "__main__":
    # Test case 1
    s1 = "anagram"
    t1 = "nagaram"
    print(f"Test 1: {is_anagram(s1, t1)}")  # Expected: True
    
    # Test case 2
    s2 = "rat"
    t2 = "car"
    print(f"Test 2: {is_anagram(s2, t2)}")  # Expected: False
    
    # Test case 3
    s3 = "aacc"
    t3 = "ccac"
    print(f"Test 3: {is_anagram(s3, t3)}")  # Expected: True