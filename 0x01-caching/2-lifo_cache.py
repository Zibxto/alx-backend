#!/usr/bin/env python3
"""BasicCache class"""
BaseCaching = __import__("base_caching").BaseCaching


class LIFOCache(BaseCaching):
    """LIFOCache that inherits from BaseCaching and is a caching system"""
    def __init__(self):
        """Constructor"""
        super().__init__()

    def put(self, key, item):
        """Add item to cache"""
        if key is not None and item is not None:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:

                # Retrieve the last item by looping through
                last_item_key = list(self.cache_data.keys())[-1]
                del self.cache_data[last_item_key]
                print("DISCARD: {}".format(last_item_key))
            self.cache_data[key] = item

    def get(self, key):
        """Get item from cache"""
        if key is None:
            return None
        else:
            return self.cache_data.get(key)
