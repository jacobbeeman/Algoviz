from visualizer import AlgorithmVisualizer
from algorithms.sorting import BubbleSort, QuickSort
from algorithms.searching import LinearSearch, BinarySearch
from algorithms.pathfinding import BFS, DFS

def main():
    algorithms = {
        "Bubble Sort": BubbleSort,
        "Quick Sort": QuickSort,
        "Linear Search": LinearSearch,
        "Binary Search": BinarySearch,
        "BFS": BFS,
        "DFS": DFS
    }

    visualizer = AlgorithmVisualizer(algorithms)
    visualizer.list_algorithms()

    while True:
        choice = input("\nEnter algorithm name (or 'exit'): ").strip()
        if choice.lower() == "exit":
            break
        elif choice in algorithms:
            visualizer.switch_algorithm(choice)
            visualizer.run(delay=0.2)
        else:
            print("❌ Invalid choice.")

if __name__ == "__main__":
    main()
