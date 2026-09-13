class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def merge_two_lists(list1, list2):
    """
    Merge two sorted linked lists and return it as a sorted list.
    The list should be made by splicing together the nodes of the first two lists.
    
    Args:
        list1: ListNode - head of the first sorted linked list
        list2: ListNode - head of the second sorted linked list
        
    Returns:
        ListNode - head of the merged sorted linked list
        
    Time Complexity: O(n + m) - where n and m are the lengths of the two lists
    Space Complexity: O(1) - constant extra space
    """
    # Create a dummy node to serve as the start of the result list
    dummy = ListNode()
    current = dummy
    
    # Traverse both lists and attach the smaller node to the result
    while list1 and list2:
        if list1.val < list2.val:
            current.next = list1
            list1 = list1.next
        else:
            current.next = list2
            list2 = list2.next
        current = current.next
    
    # Attach the remaining elements of list1 or list2
    current.next = list1 if list1 else list2
    
    return dummy.next


def create_linked_list(arr):
    """Helper function to create a linked list from an array"""
    if not arr:
        return None
    head = ListNode(arr[0])
    current = head
    for val in arr[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

def linked_list_to_array(head):
    """Helper function to convert a linked list to an array"""
    result = []
    current = head
    while current:
        result.append(current.val)
        current = current.next
    return result


if __name__ == "__main__":
    # Test case 1
    list1 = create_linked_list([1, 2, 4])
    list2 = create_linked_list([1, 3, 4])
    merged = merge_two_lists(list1, list2)
    print(f"Test 1: {linked_list_to_array(merged)}")  # Expected: [1, 1, 2, 3, 4, 4]
    
    # Test case 2
    list1 = create_linked_list([])
    list2 = create_linked_list([])
    merged = merge_two_lists(list1, list2)
    print(f"Test 2: {linked_list_to_array(merged)}")  # Expected: []
    
    # Test case 3
    list1 = create_linked_list([])
    list2 = create_linked_list([0])
    merged = merge_two_lists(list1, list2)
    print(f"Test 3: {linked_list_to_array(merged)}")  # Expected: [0]