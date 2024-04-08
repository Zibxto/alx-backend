#!/usr/bin/env python3
""" Module """
import math
from typing import List, Union
SimplePaginationServer = __import__('1-simple_pagination').Server


class Server(SimplePaginationServer):
    """Server class to paginate a database of popular baby names."""

    def get_hyper(self, page: int = 1, page_size: int = 10) -> dict:
        """Retrieve hypermedia pagination information."""
        assert isinstance(page, int) and page > 0, \
            "Page number must be a positive integer"
        assert isinstance(page_size, int) and page_size > 0, \
            "Page size must be a positive integer"

        dataset_page = self.get_page(page, page_size)
        total_pages = math.ceil(len(self.dataset()) / page_size)

        hyper_data = {
            'page_size': len(dataset_page),
            'page': page,
            'data': dataset_page,
            'next_page': page + 1 if page < total_pages else None,
            'prev_page': page - 1 if page > 1 else None,
            'total_pages': total_pages
        }

        return hyper_data
