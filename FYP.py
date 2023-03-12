from minizinc import Instance, Model, Solver
from Data import Data

MODEL_FILE = './models/fyp.mzn'
DATA_FILE = './data/fyp.dzn'
SOLVER = 'gecode'


class FYP():
    def main():
        fyp = Model(MODEL_FILE)

        Data.generate_data_file(DATA_FILE)
        fyp.add_file(DATA_FILE)

        
        gecode = Solver.lookup(SOLVER)
        instance = Instance(gecode, fyp)
        result = instance.solve()

        print(result)

    if __name__ == "__main__":
        main()

    
    