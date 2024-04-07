#!/usr/bin/env python3
"""BasicCache class"""
BaseCaching = __import__("base_caching").BaseCaching


class MRUCache(BaseCaching):
    """MRUCache that inherits from BaseCaching and is a caching system"""
    def __init__(self):
        """Constructor"""
        super().__init__()
        # List to maintain the order of keys based on usage
        self.mru_order = []

    def put(self, key, item):
        """Add item to cache"""
        if key is not None and item is not None:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                # Discard the most recently used item
                discarded_key = self.mru_order.pop()
                del self.cache_data[discarded_key]
                print("DISCARD:", discarded_key)

            # Add the item to the cache and update MRU order
            self.cache_data[key] = item
            self.mru_order.append(key)

            # Move the accessed key to the end of MRU order
            self.mru_order.remove(key)
            self.mru_order.append(key)

    def get(self, key):
        """Get item from cache"""
        if key is None or key not in self.cache_data:
            return None

        # Move the accessed key to the end of MRU order
        self.mru_order.remove(key)
        self.mru_order.append(key)

        return self.cache_data[key]
