#include <stdio.h>
#include <iostream>
#include <fstream>
#include <string>

#include "src/cpp/grid.cpp"
#include "src/cpp/check.hpp"
#include "src/cpp/algorithms.cpp"
#include "src/cpp/constants.hpp"

int main(){

    std::string rootExs = "Files/exercices/";
    std::string rootSol = "Files/solutions/";
    for (int i=0; i<N_generators;i++){
        
        std::string exs = rootExs + "ex" + std::to_string(i) + ".txt";
        std::string sol = rootSol + "sol" + std::to_string(i) + ".txt";

        int ** solution = fillGrid(N);

        int depth = rand() % (depth_max - depth_min) + depth_min;

        bool flag = false;
        int **exercice;
        int **solutionBis;
        std::cout << "Generating exercice " << i << " with depth : " << depth << std::endl;
        while (!flag){
            exercice = startGenerator(solution, N, depth);
            int** solutionBis = copy_grid(solution, N);
            fillGrid(solutionBis, N);
            flag = valid_starter(solutionBis, solution, N);
        
        }
        std::cout << "Exercice " << i << " generated" << std::endl;
        
        create_file_from_grid(exs.c_str(), exercice, N);
        create_file_from_grid(sol.c_str(), solution, N);

    }





    return 0;
}