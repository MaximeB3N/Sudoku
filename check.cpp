#include <iostream>
#include <numeric>
#include <vector>
#include "constants.hpp"

bool valid(int** grid, int n, int m, int i, int j, int value){

    if (check_row(grid, n, m, i) && check_col(grid, n, m, j) && check_box(grid, n, m, i, j)) {
        return true;
    }
    return false;

}
bool finished(int** grid, int n, int m){
    for(int i = 0; i < n; i++){
        for(int j = 0; j < m; j++){
            if(grid[i][j] == 0){
                return false;
            }
        }
    }
    return true;
}

bool check_row(int** grid, int n, int m, int i){
    std::vector<int> store;
    store.assign(m, 0);

    for(int j=0; j<m; j++){
        if (grid[i][j] == 0){
            return false;
        }
        else{
            store[grid[i][j]] = 1;
        }
    }

    if(std::accumulate(store.begin(), store.end(), 0)==9){
        return true;
    }
    else{
        return false;
    }

}
bool check_col(int** grid, int n, int m, int j){
    std::vector<int> store;
    store.assign(n, 0);

    for(int i=0; i<n; j++){
        if(grid[i][j] == 0) return false;
        
        else{
            store[grid[i][j]] = 1;
        }
    }

    if(std::accumulate(store.begin(), store.end(), 0)==9){
        return true;
    }
    else{
        return false;
    }
}
bool check_box(int** grid, int n, int m, int i, int j){
    std::vector<int> store;
    store.assign(9, 0);
    for (int k=i; k<i+3; k++){
        for(int l=j; l<j+3; l++){
            if(grid[l][k] == 0){
                return false;
            }
            else{
                store[grid[l][k]] = 1;
            }
        }
    }
    if (std::accumulate(store.begin(), store.end(), 0) == 9){
        return true;
    }
    else{
        return false;
}