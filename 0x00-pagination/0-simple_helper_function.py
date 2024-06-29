#!/usr/bin/env python3
"""Function named index_range that takes two integer
arguments page and page_size and returns tuple
"""


from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    index_range function
    """
    return ((page-1) * page_size, page_size * page)
