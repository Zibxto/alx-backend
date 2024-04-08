#!/usr/bin/env python3
"""
function named index_range that takes two integer
arguments page and page_size
"""


def index_range(page: int, page_size: int) -> tuple:
    """
    Calculate start and end indices for pagination.

    Args:
        page (int): The current page number.
        page_size (int): The number of items per page.

    Returns:
        tuple: A tuple containing start and end indices for the requested page.
    """
    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    return start_index, end_index
