// class Grid {
//     int n;
//     int** grid;

//     public:
//         Grid(int n);
//         Grid(const char* filename, int n);
//         void create_file_from_grid(const char* filename, int** grid, int n);
//         void print_grid(int** grid, int n);
//         void free_grid(int** grid, int n);
        


// };


int** create_grid(int n);
int** copy_grid(int** grid, int n);
int** create_grid_from_file(const char* filename, int n);
void create_file_from_grid(const char* filename, int** grid, int n);

void print_grid(int** grid, int n);
void free_grid(int** grid, int n);



