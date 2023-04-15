from minizinc import Instance, Model, Solver
from DataHandling import Data
import time

MODEL_FILE = './models/fyp.mzn'
DATA_FILE = './data/fyp.dzn'
SOLVER = 'gecode'
NUM_RUNS = 1

class FYP():
    def main():
        total_time = 0
        succesful_runs = 0
        
        for x in range(NUM_RUNS):
            
            ## BUILD MODEL ##
            fyp = Model(MODEL_FILE)

            # Add data file to models
            Data.generate_data_file(DATA_FILE)
            fyp.add_file(DATA_FILE)

            
            ## SOLVE INSTANCE ##
            gecode = Solver.lookup(SOLVER)
            instance = Instance(gecode, fyp)

            # Solve instance and record runtime
            start_time = time.time()
            result = instance.solve()
            runtime = round(time.time() - start_time, 3)

            ## VERIFY OUTPUT ##
            if(Data.verify_output(result)):
                print(result)
                print(f"Time: {runtime}s")
                total_time += runtime
                succesful_runs += 1
        
        #print(f"Avg Time: {round(total_time / succesful_runs, 3)}s")
        #print(result)
            

    if __name__ == "__main__":
        main()

    
    