import random

class LinearSearch:
    def __init__(self, data=None, target=None):
        self.data = data or sorted([random.randint(0, 50) for _ in range(10)])
        self.target = target or random.choice(self.data)

    def run(self):
        arr = self.data
        for i, val in enumerate(arr):
            yield f"Checking index {i}: {val}"
            if val == self.target:
                yield f"✅ Found {self.target} at index {i}"
                return
        yield f"❌ {self.target} not found."


class BinarySearch:
    def __init__(self, data=None, target=None):
        self.data = sorted(data or [random.randint(0, 50) for _ in range(10)])
        self.target = target or random.choice(self.data)

    def run(self):
        arr = self.data
        low, high = 0, len(arr) - 1
        while low <= high:
            mid = (low + high) // 2
            yield f"Checking middle index {mid}: {arr[mid]}"
            if arr[mid] == self.target:
                yield f"✅ Found {self.target} at index {mid}"
                return
            elif arr[mid] < self.target:
                low = mid + 1
            else:
                high = mid - 1
        yield f"❌ {self.target} not found."