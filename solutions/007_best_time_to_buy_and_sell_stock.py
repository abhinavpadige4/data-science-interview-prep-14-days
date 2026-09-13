def max_profit(prices):
    """
    You are given an array prices where prices[i] is the price of a given stock on the ith day.
    You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
    Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.
    
    Args:
        prices: List[int] - stock prices on each day
        
    Returns:
        int - maximum profit achievable
        
    Time Complexity: O(n) - single pass through the prices array
    Space Complexity: O(1) - constant extra space
    """
    if not prices:
        return 0
    
    min_price = prices[0]
    max_profit = 0
    
    for price in prices[1:]:
        # Calculate profit if we sell today
        profit = price - min_price
        max_profit = max(max_profit, profit)
        # Update minimum price seen so far
        min_price = min(min_price, price)
    
    return max_profit


if __name__ == "__main__":
    # Test case 1
    prices1 = [7, 1, 5, 3, 6, 4]
    print(f"Test 1: {max_profit(prices1)}")  # Expected: 5
    
    # Test case 2
    prices2 = [7, 6, 4, 3, 1]
    print(f"Test 2: {max_profit(prices2)}")  # Expected: 0
    
    # Test case 3
    prices3 = [1, 2, 3, 4, 5]
    print(f"Test 3: {max_profit(prices3)}")  # Expected: 4