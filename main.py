import numpy as np

from src.python.grid import load_grids, check_row,check_column, check_box

pathEx = "Files/exercices/ex0.txt"
pathSol = "Files/solutions/sol0.txt"

ex, sol = load_grids(pathEx, pathSol)
print(ex)


# ex[0,2] = 2
ex[2,0] = 2
print(ex)
print(check_box(ex,0,0))
print(check_column(ex,0))
print(check_row(ex,0))


print()
print(sol)
# sol[0,2] = 2
sol[2,0] = 2
print(check_box(sol,0,0))
print(check_column(sol,0))
print(check_row(sol,0))