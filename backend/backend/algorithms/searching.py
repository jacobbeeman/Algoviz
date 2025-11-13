class LinearSearch:
    def __init__(self):
        self.name = "Linear Search"

    def run(self, arr, target):
        for i in range(len(arr)):
            if arr[i] == target:
                return i
        return -1


class BinarySearch:
    def __init__(self):
        self.name = "Binary Search"

    def run(self, arr, target):
        left, right = 0, len(arr) - 1
        while left <= right:
            mid = (left + right) // 2
            if arr[mid] == target:
                return mid
            elif arr[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return -1