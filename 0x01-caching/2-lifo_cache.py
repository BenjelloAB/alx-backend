#!/usr/bin/env python3
"""Class LIFOCache that inherits from
BaseCaching and is a caching system
"""


BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    """LIFOCache class
    """

    def __init__(self):
        """__init__
        """
        super().__init__()

    def put(self, key, item):
        """put method
        """
        if key is None or item is None:
            pass
        else:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS \
                    and key not in self.cache_data.keys():
                # delete the last item in the dictionary
                last_key, last_value = self.cache_data.popitem()
                print("DISCARD: {}". format(last_key))

            self.cache_data[key] = item

    def get(self, key):
        """func that return the value in self.cache_data
        linked to key
        """
        if key is None or key not in self.cache_data.keys():
            return None
        return self.cache_data.get(key)
