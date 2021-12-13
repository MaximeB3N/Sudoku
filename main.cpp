#include <stdio.h>
#include <iostream>
#include <fstream>
#include <string>

#include "src/cpp/grid.cpp"
#include "src/cpp/check.hpp"
#include "src/cpp/algorithms.cpp"
#include "src/cpp/constants.hpp"

int main()
{
    const char *filename = "Files/exercices/ex1.txt";
    std::string root = "Files/exercices/";
    // int** grid = create_grid(N);
    // print_grid(grid, N);
    // int **grid = create_grid_from_file(filename2, N);

    // print_grid(grid, N);
    std::string name = "ex1.txt";
    std::string filename2 = root + name;
    const char *filename3 = filename2.c_str();

    int **grid = create_grid_from_file(filename3, N);

    std::cout << "filename: " << filename3 << std::endl;
    print_grid(grid, N);
    // print_grid(grid2, N);

    // int **exercice = startGenerator(solution, N, 40);
    // std::cout << "Exercice_8,8 : " << exercice[8][8] << std::endl;
    // print_grid(exercice, N);
    // // grid2[0][0] = 0;
    // // grid2[0][1] = 0;
    // // int counter = backtrackingSolver(grid2, N);
    // // std::cout << "counter: " << counter << std::endl;
    // bool flag = fillGrid(exercice, N);
    // print_grid(grid2, N);
    // print_grid(exercice, N);
    // std::cout << "flag: " << flag << std::endl;
    // for (int i = 0; i < N; i++)
    // {
    //     for (int j = 0; j < N; j++)
    //     {
    //         std::cout << (int) (exercice[i][j] == solution[i][j]);
    //     }
    //     std::cout << std::endl;
    // }
    // bool flag = false;
    // int **exercice;
    // int **solutionBis;
    // while (!flag){
    //     std::cout << "Generating new exercice" << std::endl;
    //     exercice = startGenerator(solution, N, 50);
    //     int** solutionBis = copy_grid(solution, N);
    //     fillGrid(solutionBis, N);
    //     flag = valid_starter(solutionBis, solution, N);

    // }
    // print_grid(exercice, N);
    // print_grid(solution, N);
    return 0;
}