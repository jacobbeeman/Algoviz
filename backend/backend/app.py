from flask import Flask, request, jsonify
from flask_cors import CORS

from visualizer.AlgorithmicVisualizer import AlgorithmVisualizer
from algorithms.sorting import BubbleSort, QuickSort
from algorithms.searching import LinearSearch, BinarySearch
from algorithms.pathfinding import BFS, DFS

app = Flask(__name__)
CORS(app)  # allow your GitHub Pages frontend to call the backend

# Map algorithm names to classes
ALGORITHMS = {
    "bubble_sort": BubbleSort,
    "quick_sort": QuickSort,
    "linear_search": LinearSearch,
    "binary_search": BinarySearch,
    "bfs": BFS,
    "dfs": DFS
}

# Initialize the visualizer
visualizer = AlgorithmVisualizer(ALGORITHMS)


@app.route("/api/algorithms", methods=["GET"])
def list_algorithms():
    """Return the list of available algorithms."""
    return jsonify({"algorithms": list(ALGORITHMS.keys())})


@app.route("/api/run", methods=["POST"])
def run_algorithm():
    """
    Expected JSON:
    {
        "algorithm": "bubble_sort",
        "data": [5, 1, 4, 2, 8],  # optional, if algorithm requires it
        "start": 0,              # optional (search / path)
        "end": 7                 # optional
    }
    """
    body = request.get_json()

    if not body or "algorithm" not in body:
        return jsonify({"error": "Missing algorithm name"}), 400

    name = body["algorithm"]

    if name not in ALGORITHMS:
        return jsonify({"error": f"Unknown algorithm '{name}'"}), 404

    # Switch algorithm
    visualizer.switch_algorithm(name)

    # Run the algorithm and capture steps from the visualizer
    try:
        # Pass only arguments your AlgorithmVisualizer supports
        steps = visualizer.run_api(body)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

    return jsonify({
        "algorithm": name,
        "steps": steps
    })


if __name__ == "__main__":
    app.run(debug=True, port=5000)