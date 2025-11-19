class LinearSearch:
    def __init__(self):
        self.name = "Linear Search"

    def run(self, arr, target):
        for i in range(len(arr)):
            # Yield each inspection step
            yield {
                "array": arr[:],
                "index": i,
                "value": arr[i],
                "target": target,
                "found": arr[i] == target
            }

            if arr[i] == target:
                return

        # Final step if not found
        yield {
            "array": arr[:],
            "index": None,
            "value": None,
            "target": target,
            "found": False
        }



class BinarySearch:
    def __init__(self):
        self.name = "Binary Search"

    def run(self, arr, target):
        left, right = 0, len(arr) - 1
        arr_copy = arr[:]  # prevent mutation

        while left <= right:
            mid = (left + right) // 2

            # yield visualizer step
            yield {
                "array": arr_copy,
                "left": left,
                "mid": mid,
                "right": right,
                "value_at_mid": arr_copy[mid],
                "target": target,
                "found": arr_copy[mid] == target
            }

            if arr_copy[mid] == target:
                return

            elif arr_copy[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        # not found
        yield {
            "array": arr_copy,
            "left": left,
            "mid": None,
            "right": right,
            "value_at_mid": None,
            "target": target,
            "found": False
        }
