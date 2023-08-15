def saturate(value: int, min_value: int, max_value: int) -> int:
    """
    >>> saturate(50, 10, 100)
    50
    >>> saturate(7, 10, 100)
    10
    >>> saturate(200, 10, 100)
    100
    """
    return min(max(value, min_value), max_value)
