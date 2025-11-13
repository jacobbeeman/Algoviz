class BubbleSort:
    def __init__(self):
        self.name = "Bubble Sort"

    def run(self, arr):
        n = len(arr)
        for i in range(n):
            for j in range(0, n - i - 1):
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
                    yield arr  # useful for animations (each step)
        yield arr


class QuickSort:
    def __init__(self):
        self.name = "Quick Sort"

    def run(self, arr):
        yield from self._quicksort(arr, 0, len(arr) - 1)
        yield arr

    def _quicksort(self, arr, low, high):
        if low < high:
            pi = self._partition(arr, low, high)
            yield arr
            yield from self._quicksort(arr, low, pi - 1)
            yield from self._quicksort(arr, pi + 1, high)

    def _partition(self, arr, low, high):
        pivot = arr[high]
        i = low - 1
        for j in range(low, high):
            if arr[j] < pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        return i + 1