import numpy as np

from src.python.constants import N

def load_grids(pathEx, pathSol, unsqueeze=True):
    """
    Loads the grids from the files
    """
    # Load the grid
    gridEx = np.genfromtxt(pathEx, delimiter=' ', dtype=np.int)
    gridSol = np.genfromtxt(pathSol, delimiter=' ', dtype=np.int)

    if unsqueeze:
        gridEx = np.expand_dims(gridEx, axis=-1)
        gridSol = np.expand_dims(gridSol, axis=-1)
    # Return the grids
    return gridEx, gridSol

def valid(grid, i, j):
    return check_row(grid, i) and check_column(grid, j) and check_box(grid, i, j)


def finished(grid):
    """
    Checks if the grid is finished
    """
    # Check if the grid is finished
    return not np.any(grid == 0)

def get_empty_cell(grid):
    """
    Returns the positions of the empty cell
    """
    # Get the position of the first empty cell
    pos = np.argwhere(grid == 0)

    # Return the position
    return pos

def check_row(grid, i):

    counts = np.bincount(grid[i, :])
    if 0 in grid[i,:]:
        
        if len(counts) == 1:
            return True
    
        return np.all(counts[1:] <= 1)

    else:
        return np.all(counts[1:] == 1) and counts[0] == 0
    

def check_column(grid, j):
    counts = np.bincount(grid[:, j])
    if 0 in grid[:,j]:
        
        if len(counts) == 1:
            return True
    
        return np.all(counts[1:] <= 1)

    else:
        return np.all(counts[1:] == 1) and counts[0] == 0

def check_box(grid, i, j):

    box_size = int(np.sqrt(N))

    row = (i // box_size)*box_size
    col = (j // box_size)*box_size
    subgrid = grid[row:row+box_size, col:col+box_size]
    counts = np.bincount(subgrid.flatten())
    if 0 in subgrid:   
        if len(counts) == 1:
            return True
    
        return np.all(counts[1:] <= 1)

    else:
        return np.all(counts[1:] == 1) and counts[0] == 0


