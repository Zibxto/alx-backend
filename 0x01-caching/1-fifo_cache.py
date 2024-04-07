#!/usr/bin/env python3
"""BasicCache class"""
BaseCaching = __import__("base_caching").BaseCaching


class FIFOCache(BaseCaching):
    """FIFOCache that inherits from BaseCaching and is a caching system"""
    def __init__(self):
        """Constructor"""
        super().__init__()

    def put(self, key, item):
        """Add item to cache"""
        if key is not None and item is not None:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                # Get an iterator for the dictionary items
                iterator = iter(self.cache_data.items())

                # Retrieve the first item using next()
                first_item_key, _ = next(iterator)
                del self.cache_data[first_item_key]
                print("DISCARD: {}".format(first_item_key))
            self.cache_data[key] = item

    def get(self, key):
        """Get item from cache"""
        if key is None:
            return None
        else:
            return self.cache_data.get(key)
