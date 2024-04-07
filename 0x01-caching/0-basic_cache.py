#!/usr/bin/env python3
"""BasicCache class"""
BaseCaching = __import__("base_caching").BaseCaching


class BasicCache(BaseCaching):
    """BasicCache that inherits from BaseCaching and is a caching system"""
    def __init__(self):
        """Constructor"""
        super().__init__()

    def put(self, key, item):
        """Add item to cache"""
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """Get item from cache"""
        if key is None:
            return None
        else:
            return self.cache_data.get(key)
