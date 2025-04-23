# Last updated: 4/23/2025, 2:09:28 PM
import collections
def calculate_digit_sum(num: int) -> int:
    """
    Computes the sum of the digits of a given number.

    Parameters:
    num (int): The number for which to calculate the digit sum.

    Returns:
    int: The sum of the digits of the number.

    Example:
    >>> calculate_digit_sum(123)
    6
    """
    return sum(int(digit) for digit in str(num))

def group_numbers_by_digit_sum(n: int) -> dict:
    """
    Groups numbers from 1 to n based on their digit sums.

    Parameters:
    n (int): The upper limit of the range (inclusive).

    Returns:
    dict: A dictionary where keys are digit sums and values are lists of numbers with that digit sum.

    Example:
    >>> group_numbers_by_digit_sum(13)
    {1: [1, 10], 2: [2, 11], 3: [3, 12], 4: [4, 13], 5: [5], 6: [6], 7: [7], 8: [8], 9: [9]}
    """
    groups = {}
    
    for num in range(1, n + 1):
        digit_sum = sum(int(digit) for digit in str(num))
        if digit_sum not in groups:
            groups[digit_sum] = []
        groups[digit_sum].append(num)
    
    return groups

def count_largest_groups(groups: dict) -> int:
    """
    Counts how many groups have the largest size.

    Parameters:
    groups (dict): A dictionary of groups where keys are digit sums and values are lists of numbers.

    Returns:
    int: The count of groups that have the largest size.

    Example:
    >>> count_largest_groups({1: [1, 10], 2: [2, 11], 3: [3, 12], 4: [4, 13]})
    4
    """
    if not groups:
        return 0  # Return 0 if there are no groups

    max_size = max(len(group) for group in groups.values())  # Find the maximum group size
    count = sum(1 for group in groups.values() if len(group) == max_size)  # Count groups of that size

    return count

def largest_digit_sum_groups(n: int) -> int:
    """
    Orchestrates the grouping of numbers by digit sum and counts the largest groups.

    Parameters:
    n (int): The upper limit of the range (inclusive).

    Returns:
    int: The number of groups that have the largest size.

    Example:
    >>> largest_digit_sum_groups(13)
    4
    """
    # Group numbers by their digit sums
    groups = group_numbers_by_digit_sum(n)
    
    # Count how many groups have the largest size
    return count_largest_groups(groups)

class Solution:
    def countLargestGroup(self, n: int) -> int:
        return largest_digit_sum_groups(n)