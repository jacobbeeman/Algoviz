import random


class BubbleSort:
    def __init__(self, data=None):
        self.data = data or [random.randint(0, 50) for _ in range(10)]

    def run(self):
        arr = self.data.copy()
        n = len(arr)
        for i in range(n):
            for j in range(n - i - 1):
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
                yield arr.copy()


class QuickSort:
    def __init__(self, data=None):
        self.data = data or [random.randint(0, 50) for _ in range(10)]

    def run(self):
        arr = self.data.copy()
        yield from self._quick_sort(arr, 0, len(arr) - 1)

    def _quick_sort(self, arr, low, high):
        if low < high:
            p = self._partition(arr, low, high)
            yield arr.copy()
            yield from self._quick_sort(arr, low, p - 1)
            yield from self._quick_sort(arr, p + 1, high)

    def _partition(self, arr, low, high):
        pivot = arr[high]
        i = low - 1
        for j in range(low, high):
            if arr[j] < pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        return i + 1