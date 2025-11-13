from flask import Flask, request, jsonify, render_template
from flask_cors import CORS

from visualizer.AlgorithmicVisualizer import AlgorithmVisualizer
from algorithms.sorting import BubbleSort, QuickSort
from algorithms.searching import LinearSearch, BinarySearch
from algorithms.pathfinding import BFS, DFS

app = Flask(__name__)
CORS(app)

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

@app.route("/")
def home():
    return "Backend is running!"

@app.route("/api/algorithms", methods=["GET"])
def list_algorithms():
    return jsonify({"algorithms": list(ALGORITHMS.keys())})

@app.route("/api/run", methods=["POST"])
def run_algorithm():
    body = request.get_json()

    if not body or "algorithm" not in body:
        return jsonify({"error": "Missing algorithm name"}), 400

    name = body["algorithm"]

    if name not in ALGORITHMS:
        return jsonify({"error": f"Unknown algorithm '{name}'"}), 404

    visualizer.switch_algorithm(name)

    try:
        steps = visualizer.run_api(body)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

    return jsonify({
        "algorithm": name,
        "steps": steps
    })

if __name__ == "__main__":
    # Use 0.0.0.0 for Render deployment
    app.run(host="0.0.0.0", port=5000, debug=True)