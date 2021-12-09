#include <iostream>
#include <stdio.h>
#include <stdlib.h>

int** create_grid(int n, int m){
    int** grid = new int*[n];
    for(int i = 0; i < n; i++){
        grid[i] = new int[m];
    }
    return grid;
}

int** create_random_grid(int n, int m){
    int** grid = new int*[n];
    for(int i = 0; i < n; i++){
        grid[i] = new int[m];
        for(int j = 0; j < m; j++){
            grid[i][j] = rand() % 10;
        }
    }
    return grid;
}

int** create_grid_from_file(const char* filename, int n, int m){
    int** grid = create_grid(n,m);
    int a = 0;
    FILE* fp = fopen(filename, "r");

    for(int i = 0; i < n; i++){
        grid[i] = new int[m];
        for(int j = 0; j < m; j++){
            fscanf(fp, "%d", &grid[i][j]);

        }    
    }
    fclose(fp);
    return grid;
}

void create_file_from_grid(const char* filename, int** grid, int n, int m){
    FILE* fp = fopen(filename, "w");
    for(int i = 0; i < n; i++){
        for(int j = 0; j < m; j++){
            fprintf(fp, "%d ", grid[i][j]);
        }
        fprintf(fp, "\n");
    }
    fclose(fp);
}

void print_grid(int** grid, int n, int m){ 
    for(int i = 0; i < n; i++){
        for(int j = 0; j < m; j++){
            std::cout << grid[i][j] << " ";
        }
        std::cout << std::endl;
    }
    std::cout << std::endl;
}

void free_grid(int** grid, int n){
    for(int i = 0; i < n; i++){
        delete[] grid[i];
    }
    delete[] grid;
}
void fill_grid(int** grid, int n, int m, int value){
    grid[n][m] = value;
}