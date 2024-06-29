#!/usr/bin/env python3
"""Create a class BasicCache that inherits from
BaseCaching and is a caching system
"""


BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """BasicCache Class
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
            self.cache_data[key] = item

    def get(self, key):
        """func that returns the value in self.cache_data
        linked to key
        """
        if key is None or key not in self.cache_data.keys():
            return None
        return self.cache_data.get(key)
