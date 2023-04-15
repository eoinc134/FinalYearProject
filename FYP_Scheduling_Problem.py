from minizinc import Instance, Model, Solver
from DataHandling import Data
import time

MODEL_FILE = './models/fyp.mzn'
DATA_FILE = './data/fyp.dzn'
SOLVER = 'gecode'
NUM_RUNS = 1

def main():
    """
    Runs the MiniZinc instance NUM_RUNS times and prints the average runtime.
    """
    total_time = 0
    successful_runs = 0
    
    for _ in range(NUM_RUNS):
        model = build_model()
        result, runtime = solve_instance(model)
        if verify_output(result):
            print_result(result, runtime)
            total_time += runtime
            successful_runs += 1
    
    if successful_runs > 0:
        if NUM_RUNS == 1:
            print("Single run completed.")
        else:
            print(f"Avg Time: {round(total_time / successful_runs, 3)}s")
    else:
        print("No successful runs.")


def build_model():
    """
    Builds the MiniZinc model and adds the data file to it.
    """
    fyp = Model(MODEL_FILE)
    Data.generate_data_file(DATA_FILE)
    fyp.add_file(DATA_FILE)
    return fyp


def solve_instance(model):
    """
    Solves the MiniZinc instance given the model.
    """
    gecode = Solver.lookup(SOLVER)
    instance = Instance(gecode, model)

    start_time = time.time()
    result = instance.solve()
    runtime = round(time.time() - start_time, 3)

    return result, runtime


def verify_output(result):
    """
    Verifies that the output of the MiniZinc instance is correct.
    """
    return Data.verify_output(result)


def print_result(result, runtime):
    """
    Prints the solution and runtime.
    """
    if NUM_RUNS == 1:
        print(result)
    print(f"Time: {runtime}s")          


if __name__ == "__main__":
    main()

    
    