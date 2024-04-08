#!/usr/bin/env python3
""" Module """
import csv
import math
from typing import List
index_range = __import__('0-simple_helper_function').index_range


class Server:
    """Server class to paginate a database of popular baby names."""
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        """Construtor"""
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset."""
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """Retrieve a specific page of data from the dataset."""
        assert isinstance(page, int) and page > 0, \
            "Page number must be a positive integer"
        assert isinstance(page_size, int) and page_size > 0, \
            "Page size must be a positive integer"

        dataset = self.dataset()
        total_entries = len(dataset)
        total_pages = math.ceil(total_entries / page_size)

        if page > total_pages:
            return []

        start, end = index_range(page, page_size)
        return dataset[start:end]
