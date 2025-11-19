import time

class AlgorithmVisualizer:
    def __init__(self, algorithms):
        self.algorithms = algorithms
        self.current_name = list(algorithms.keys())[0]
        self.current_algorithm = algorithms[self.current_name]()

    def switch_algorithm(self, name):
        if name not in self.algorithms:
            raise ValueError(f"Algorithm '{name}' not found.")
        self.current_name = name
        self.current_algorithm = self.algorithms[name]()

    def run_api(self, body):
        """Normalize steps for frontend animations."""
        if "data" not in body:
            raise ValueError("Missing 'data' in request body.")

        data = body["data"]
        target = body.get("target", None)
        algo = self.current_algorithm

        # Support search algorithms (which take target)
        try:
            raw_steps = algo.run(data, target) if target is not None else algo.run(data)
        except TypeError:
            raw_steps = algo.run(data)

        # Convert generator → list
        if hasattr(raw_steps, "__iter__") and not isinstance(raw_steps, list):
            raw_steps = list(raw_steps)

        # Normalize output for frontend
        steps = []
        for step in raw_steps:
            if isinstance(step, dict):
                steps.append(step)  # search steps like {"mid":..., "left":..., "right":...}
            else:
                steps.append({"array": step})  # sorting steps like [1,4,3,2]

        return steps

    def run(self, delay=0.1):
        print(f"\nRunning {self.current_name}...\n")
        for step in self.current_algorithm.run():
            print(step)
            time.sleep(delay)
        print(f"\n✅ {self.current_name} complete.\n")

    def list_algorithms(self):
        print("Available algorithms:")
        for name in self.algorithms:
            print(f"- {name}")
