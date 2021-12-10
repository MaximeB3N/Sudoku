#include <iostream>
#include <stdio.h>
#include <stdlib.h>
#include <vector>
#include <algorithm>
#include <random>

#include "algorithms.hpp"
#include "grid.hpp"
#include "check.cpp"

int** fillGrid(int n){
    int** grid;
    bool flag = false;
    while (!flag){
        grid = create_grid(n);   
        flag = fillGrid(grid, n);
    }
    return grid;
}

bool fillGrid(int** grid, int n) {

    // We create the list of all possible values
    std::vector<int> numberList;
    for(int i = 1; i < n+1; i++){
        numberList.push_back(i);
    }
    for (int i = 0; i < n; i++){
        for (int j = 0; j < n; j++){
            // If the cell is empty, we fill it with a random value
            if (grid[i][j]==0){
                std::shuffle(numberList.begin(), numberList.end(), std::default_random_engine(std::random_device()()));
                for (int k = 0; k < n; k++){
                    grid[i][j] = numberList[k];
                    if (valid(grid, n, i, j)){
                        // In that case we found a solution
                        if (finished(grid,n)){
                            return true;
                        }
                        // In that case we found a solution using numberList[k] at i,j
                        // The grid is already filled using recursive calls
                        if (fillGrid(grid, n)){
                            return true;
                        }

                        // If both cases above failed, thus we try another value

                    }
                    else {
                        // In that case we tried every value in numberList[k] at i,j and none of them worked
                        // We reset the cell to 0, then return false to go back the previous recursive call
                        if (k==n-1){
                            grid[i][j] = 0;
                            return false;
                        } 
                    }
                }

            }
        }
    }
    // This case should never happen
    std::cout << "Error: fillGrid() failed" << std::endl;
    return false;
}

int backtrackingSolver(int **grid, int n){
    std::vector<int> counter;
    int ** grid_copy = create_grid(n);
    for (int i = 0; i < n; i++){
        for (int j = 0; j < n; j++){
            grid_copy[i][j] = grid[i][j];
        }
    }
    backtrackingSolver(grid_copy, n, counter);

    return counter.size();

}
bool backtrackingSolver(int **grid, int n, std::vector<int> counter){
    // We create the list of all possible values
    std::vector<int> numberList;
    for(int i = 1; i < n+1; i++){
        numberList.push_back(i);
    }
    for (int i = 0; i < n; i++){
        for (int j = 0; j < n; j++){
            // If the cell is empty, we fill it with a random value
            if (grid[i][j]==0){
                std::shuffle(numberList.begin(), numberList.end(), std::default_random_engine(std::random_device()()));
                for (int k = 0; k < n; k++){
                    grid[i][j] = numberList[k];
                    if (valid(grid, n, i, j)){
                        // In that case we found a solution
                        if (finished(grid,n)){
                            counter.push_back(1);
                            return true;
                        }
                        // In that case we found a solution using numberList[k] at i,j
                        // The grid is already filled using recursive calls
                        if (backtrackingSolver(grid, n, counter)){
                            return true;
                        }

                        // If both cases above failed, thus we try another value

                    }
                    else {
                        // In that case we tried every value in numberList[k] at i,j and none of them worked
                        // We reset the cell to 0, then return false to go back the previous recursive call
                        if (k==n-1){
                            grid[i][j] = 0;
                            return false;
                        } 
                    }
                }

            }
        }
    }
    // This case should never happen
    std::cout << "Error: fillGrid() failed" << std::endl;
    return false;


}