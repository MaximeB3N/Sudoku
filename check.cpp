#include <iostream>
#include <numeric>
#include <vector>

#include "check.hpp"

bool valid(int** grid, int n, int i, int j){

    if (check_row(grid, n, i) && check_col(grid, n, j) && check_box(grid, n, i, j)) {
        return true;
    }
    return false;

}
bool finished(int** grid, int n){
    for(int i = 0; i < n; i++){
        for(int j = 0; j < n; j++){
            if(grid[i][j] == 0){
                return false;
            }
        }
    }
    return true;
}

bool check_row(int** grid, int n, int i){
    std::vector<int> store;
    store.assign(n, 0);

    for(int j=0; j<n; j++){
        if (grid[i][j] == 0) {
            continue;
        }
        else if (store[grid[i][j]-1] == 1){
            return false;
        }
        else{
            store[grid[i][j]-1] = 1;
        }
    } 
    return true;
}

bool check_col(int** grid, int n, int j){
    std::vector<int> store;
    store.assign(n, 0);

    for(int i=0; i<n; i++){
        if (grid[i][j] == 0) {
            continue;
        }
        else if (store[grid[i][j]-1] == 1){
            return false;
        }
        else{
            store[grid[i][j]-1] = 1;
        }    
    }
    return true;
}

bool check_box(int** grid, int n, int i, int j){
    std::vector<int> store;
    int block_size = std::sqrt(n);
    store.assign(n, 0);
    int row = i - i%3;
    int col = j - j%3;

    // std::cout << "row: " << row << " col: " << col << std::endl;
    for (int k=row; k<row+block_size; k++){
        for(int l=col; l<col+block_size; l++){
            if (grid[k][l] == 0){
                continue;
            }
            // std::cout << "store :" <<store[grid[l][k]-1] << std::endl;

            if(store[grid[k][l]-1] == 1){
                return false;
            }
            else{
                store[grid[k][l]-1] = 1;
            }
        }
    }
    return true;
}

bool check_removable(int** grid, int n, int i, int j){
    int value = grid[i][j];
    for (int l=1; l<n+1; l++){
        if (grid[i][j] != l){
            grid[i][j] = l;
            // In that case, it may be possible to have multiple solutions  
            if (valid(grid, n, i, j)){
                return false;
            }
        }
    }
    // In that case, value is the only possible value
    grid[i][j] = value;
    return true;
}