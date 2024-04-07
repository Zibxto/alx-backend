#!/usr/bin/env python3
"""BasicCache class"""
BaseCaching = __import__("base_caching").BaseCaching


class LFUCache(BaseCaching):
    """LFUCache that inherits from BaseCaching and is a caching system"""

    def __init__(self):
        """Constructor"""
        super().__init__()
        # Dictionary to store the frequency of each key
        self.frequency = {}

    def put(self, key, item):
        """Add item to cache"""
        if key is not None and item is not None:
            # Increment the frequency count for the key
            self.frequency[key] = self.frequency.get(key, 0) + 1

            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                # Find the item(s) with the least frequency count
                min_frequency = min(self.frequency.values())
                least_frequent_items = [k for k, v in
                                        self.frequency.items()
                                        if v == min_frequency]

                # If there are multiple least frequent items
                # use LRU to discard the least recently used
                if least_frequent_items:
                    if len(least_frequent_items) > 1:
                        # Find the least recently used key among
                        # the least frequent items
                        discarded_key = min(least_frequent_items,
                                            key=lambda k:
                                            (self.frequency.get(k, 0), k))
                        if discarded_key in self.cache_data:
                            del self.cache_data[discarded_key]
                            del self.frequency[discarded_key]
                            print("DISCARD:", discarded_key)
                    else:
                        # Discard the least frequent item
                        key_to_discard = least_frequent_items[0]
                        if key_to_discard in self.cache_data:
                            del self.cache_data[key_to_discard]
                            del self.frequency[key_to_discard]
                            print("DISCARD:", key_to_discard)

            # Add the item to the cache
            self.cache_data[key] = item

    def get(self, key):
        """Get item from cache"""
        if key is None or key not in self.cache_data:
            return None

        # Increment the frequency count for the key
        self.frequency[key] = self.frequency.get(key, 0) + 1

        return self.cache_data[key]
