from minizinc import Instance, Model, Solver
from Availability import Availability

class FYP():
    def main():
        fyp = Model("./models/fyp.mzn")
        fyp.add_file("./models/fyp.dzn")

        Availability.generate_availability("./DataFiles/availability.csv")

        gecode = Solver.lookup("gecode")
        instance = Instance(gecode, fyp)
        result = instance.solve()

        print(result)

    if __name__ == "__main__":
        main()

    
    