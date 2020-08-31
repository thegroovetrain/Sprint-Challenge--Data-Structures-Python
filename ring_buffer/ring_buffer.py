class RingBuffer:
    def __init__(self, capacity):
        self.storage = []
        self.pointer = 0
        self.capacity = capacity

    def append(self, item):
        if len(self.storage) < self.capacity:
            self.storage.append(item)
        else:
            self.storage[self.pointer % self.capacity] = item
        self.pointer += 1

    def get(self):
        return self.storage
