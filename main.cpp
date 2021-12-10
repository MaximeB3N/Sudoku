#include <stdio.h>
#include <iostream>
#include <fstream>
#include <string>

#include "grid.cpp"
#include "check.hpp"
#include "algorithms.cpp"
#include "constants.hpp"

int main()
{
    const char *filename = "Files/exercices/ex1.txt";
    const char *filename2 = "Files/solutions/sol1.txt";

    // int** grid = create_grid(N);
    // print_grid(grid, N);
    int **grid = create_grid_from_file(filename2, N);

    print_grid(grid, N);

    int **grid2 = fillGrid(N);
    print_grid(grid2, N);
    grid2[0][0] = 0;
    grid2[0][1] = 0;
    int counter = backtrackingSolver(grid2, N);
    std::cout << "counter: " << counter << std::endl;


    return 0;
}