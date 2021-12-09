#include <iostream>
#include <stdio.h>
#include <stdlib.h>

int** create_grid(int n){
    int** grid = new int*[n];
    for(int i = 0; i < n; i++){
        grid[i] = new int[n];
        for (int j = 0; j < n; j++){
            grid[i][j] = 0;
        }
    }
    return grid;
}

int** create_random_grid(int n){
    int** grid = new int*[n];
    for(int i = 0; i < n; i++){
        grid[i] = new int[n];
        for(int j = 0; j < n; j++){
            grid[i][j] = rand() % 10;
        }
    }
    return grid;
}

int** create_grid_from_file(const char* filename, int n){
    int** grid = create_grid(n);
    int a = 0;
    FILE* fp = fopen(filename, "r");

    for(int i = 0; i < n; i++){
        grid[i] = new int[n];
        for(int j = 0; j < n; j++){
            fscanf(fp, "%d", &grid[i][j]);

        }    
    }
    fclose(fp);
    return grid;
}

void create_file_from_grid(const char* filename, int** grid, int n){
    FILE* fp = fopen(filename, "w");
    for(int i = 0; i < n; i++){
        for(int j = 0; j < n; j++){
            fprintf(fp, "%d ", grid[i][j]);
        }
        fprintf(fp, "\n");
    }
    fclose(fp);
}

void print_grid(int** grid, int n){ 
    for(int i = 0; i < n; i++){
        for(int j = 0; j < n; j++){
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
void fill_grid(int** grid, int i, int j, int value){
    grid[i][j] = value;
}