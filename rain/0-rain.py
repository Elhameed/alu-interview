#!/usr/bin/python3

def rain(walls):

    """
    Calculate the total amount of rainwater retained between walls.

    Args:
        walls (List[int]): A list of non-negative integers representing the heights of walls.

    Returns:
        int: The total amount of rainwater retained.

    Note:
        - If the input list is empty, the function returns 0.
        - The ends of the list (before index 0 and after index walls[-1]) are not considered walls.

    Example:
        >>> walls = [0, 1, 0, 2, 0, 3, 0, 4]
        >>> rain(walls)
        6

    """
  
    if not walls:
        return 0

    n = len(walls)
    left_max = [0] * n
    right_max = [0] * n

    left_max[0] = walls[0]
    for i in range(1, n):
        left_max[i] = max(left_max[i - 1], walls[i])

    right_max[n - 1] = walls[n - 1]
    for i in range(n - 2, -1, -1):
        right_max[i] = max(right_max[i + 1], walls[i])

    total_water = 0
    for i in range(n):
        total_water += min(left_max[i], right_max[i]) - walls[i]

    return total_water

# Test cases
if __name__ == "__main__":
    walls1 = [0, 1, 0, 2, 0, 3, 0, 4]
    print(rain(walls1))  # Output: 6

    walls2 = [2, 0, 0, 4, 0, 0, 1, 0]
    print(rain(walls2))  # Output: 6
