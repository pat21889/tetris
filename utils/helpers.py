from typing import TypeVar

numeric = TypeVar('numeric', int, float)

def clamp(value: numeric, min_val: numeric, max_val: numeric) -> numeric:
    if min_val <= value <= max_val:
        return value
    return min_val if value < min_val else max_val