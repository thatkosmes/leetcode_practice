from typing import List

# -------------------------------
# Solution function
# -------------------------------
def min_operations(nums: List[int], k: int) -> int:
    """
    Returns the minimum number of operations to make the sum of 'nums' divisible by 'k'.
    
    In one operation, you can decrease any element by 1.  
    The function calculates the fewest operations needed to satisfy divisibility.
    
    Args:
        nums (list of int): List of positive integers.
        k (int): The divisor.

    Returns:
        int: Minimum number of decrement operations required.
    """
    return sum(nums) % k

# -------------------------------
# Local tests
# -------------------------------
def test_min_operations():
    assert min_operations([3, 1, 4], 2) == 0
    assert min_operations([1, 1, 2, 1], 3) == 2
    assert min_operations([1, 4, 3], 5) == 3
    print("All tests passed!")

# -------------------------------
# Run tests if executed as main
# -------------------------------
if __name__ == "__main__":
    test_min_operations()