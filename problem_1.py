class LRU_Cache(object):
    def __init__(self, capacity):
        # Initialize class variables
        self.data = {}
        self.capacity = capacity
        pass

    def remove_lowest(self):

        min_value = sorted(self.data.values())[0]
        for key, value in dict(self.data).items():
            if value == min_value:
                del self.data[key]
                return

    def get(self, key):
        if key in self.data:
            count = self.data[key][0] + 1
            self.data[key][0] = count
            return self.data[key][1]
        else:
            return -1
        # Retrieve item from provided key. Return -1 if nonexistent.

    def set(self, key, value):
        # Set the value if the key is not present in the cache. If the cache is at capacity remove the oldest item
        if key in self.data:
            count = self.data[key][0] + 1
            self.data[key] = [count, value]
        else:
            if len(self.data) == self.capacity:
                # remove one
                self.remove_lowest()
            self.data[key] = [0, value]


our_cache = LRU_Cache(5)

our_cache.set(1, 11)
our_cache.set(2, 2)
our_cache.set(3, 3)
our_cache.set(4, 4)

print(our_cache.get(1))  # returns 1
print(our_cache.get(2))  # returns 2
print(our_cache.get(9))  # returns -1 because 9 is not present in the cache

our_cache.set(5, 5)
our_cache.set(6, 6)

print(our_cache.get(3))  # returns -1
our_cache.set(15, 15)
print(our_cache.get(5))
our_cache.set(7, 7)

print(our_cache.get(6))  # returns -1
