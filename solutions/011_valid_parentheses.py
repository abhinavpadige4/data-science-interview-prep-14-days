def is_valid(s):
    """
    Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
    An input string is valid if:
    1. Open brackets must be closed by the same type of brackets.
    2. Open brackets must be closed in the correct order.
    
    Args:
        s: str - string containing only brackets
        
    Returns:
        bool - True if the string is valid, False otherwise
        
    Time Complexity: O(n) - single pass through the string
    Space Complexity: O(n) - stack storage
    """
    if not s:
        return True
    
    # Mapping of closing brackets to their corresponding opening brackets
    bracket_map = {')': '(', '}': '{', ']': '['}
    # Stack to keep track of opening brackets
    stack = []
    
    for char in s:
        if char in bracket_map:
            # If it's a closing bracket
            top_element = stack.pop() if stack else '#'
            if bracket_map[char] != top_element:
                return False
        else:
            # If it's an opening bracket, push to stack
            stack.append(char)
    
    # If stack is empty, all brackets were properly closed
    return not stack


if __name__ == "__main__":
    # Test case 1
    s1 = "()"
    print(f"Test 1: {is_valid(s1)}")  # Expected: True
    
    # Test case 2
    s2 = "()[]{}"
    print(f"Test 2: {is_valid(s2)}")  # Expected: True
    
    # Test case 3
    s3 = "(]"
    print(f"Test 3: {is_valid(s3)}")  # Expected: False
    
    # Test case 4
    s4 = "([)]"
    print(f"Test 4: {is_valid(s4)}")  # Expected: False
    
    # Test case 5
    s5 = "{[]}"
    print(f"Test 5: {is_valid(s5)}")  # Expected: True