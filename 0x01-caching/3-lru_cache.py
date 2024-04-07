#!/usr/bin/env python3
"""BasicCache class"""
BaseCaching = __import__("base_caching").BaseCaching


class LRUCache(BaseCaching):
    """LRUCache that inherits from BaseCaching and is a caching system"""
    def __init__(self):
        """Constructor"""
        super().__init__()
        # List to maintain the order of keys based on usage
        self.lru_order = []

    def put(self, key, item):
        """Add item to cache"""
        if key is not None and item is not None:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:

                discarded_key = self.lru_order.pop(0)
                del self.cache_data[discarded_key]
                print("DISCARD:", discarded_key)

            # Add the item to the cache and update LRU order
            self.cache_data[key] = item
            self.lru_order.append(key)

    def get(self, key):
        """Get item from cache"""
        if key is None or key not in self.cache_data:
            return None
        # Move the accessed key to the end of LRU order
        self.lru_order.remove(key)
        self.lru_order.append(key)

        return self.cache_data[key]
