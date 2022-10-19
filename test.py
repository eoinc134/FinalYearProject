from minizinc import Instance, Model, Solver

# Load n-Queens model from file
nqueens = Model("MiniZincModels/nqueens.mzn")
# Find the MiniZinc solver configuration for Gecode
gecode = Solver.lookup("gecode")
# Create an Instance of the n-Queens model for Gecode
instance = Instance(gecode, nqueens)
# Assign 4 to n
instance["n"] = 6

result = instance.solve(all_solutions=True)
# Output the array q
for i in range(len(result)):
    print(result[i, "q"])
# print(result["q"])