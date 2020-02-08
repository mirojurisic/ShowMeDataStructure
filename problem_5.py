import hashlib
from datetime import datetime


class Block_list:
    def __init__(self):
        self.root = None
        self.next = None

    def add_block(self, block):
        if self.root is None:
            self.root = block
        node = self.root
        parent = None
        while node:
            parent = node
            node = self.next
        self.root = block


class Block:

    def __init__(self, timestamp, data, previous_hash):
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calc_hash(data)

    def calc_hash(self, data):
        sha = hashlib.sha256()
        hash_str = data.encode('utf-8')
        sha.update(hash_str)
        return sha.hexdigest()

    def get_utc_time(self):
        return self.timestamp

# Null, a single block, and multiple block inputs.
