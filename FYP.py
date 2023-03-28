from minizinc import Instance, Model, Solver
from Data import Data
import time

MODEL_FILE = './models/fyp.mzn'
DATA_FILE = './data/fyp.dzn'
SOLVER = 'gecode'
NUM_RUNS = 5

class FYP():
    def main():
        total_time = 0
        succesful_runs = 0
        
        for x in range(NUM_RUNS):
            start_time = time.time()
            ## BUILD MODEL ##
            fyp = Model(MODEL_FILE)

            Data.generate_data_file(DATA_FILE)
            fyp.add_file(DATA_FILE)

            
            ## SOLVE INSTANCE ##
            gecode = Solver.lookup(SOLVER)
            instance = Instance(gecode, fyp)
            result = instance.solve()

            ## VERIFY OUTPUT ##
            if(Data.verify_output(result)):
                #print(result)
                runtime = round(time.time() - start_time, 3)
                print(f"Time: {runtime}s")
                total_time += runtime
                succesful_runs += 1
        
        print(f"Avg Time: {round(total_time / succesful_runs, 3)}s")

            

    if __name__ == "__main__":
        main()

    
    