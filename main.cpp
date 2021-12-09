#include <stdio.h>
#include <iostream>
#include <fstream>
#include <string>

#include "grid.cpp"
#include "constants.hpp"

int main()
{
    const char *filename = "Files/exercices/ex1.txt";
    const char *filename2 = "Files/exercices/ex2.txt";
    int** grid = create_grid_from_file(filename, N, M);
    print_grid(grid, N, M);

    int **rand_grid = create_random_grid(N, M);
    print_grid(rand_grid, N, M);
    create_file_from_grid(filename2, rand_grid, N, M);
    

    

    return 0;
}